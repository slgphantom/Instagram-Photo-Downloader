import requests
import json
import os
import errno
from PIL import Image
from StringIO import StringIO
import sys





username = ''



def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def make_sure_json_exists(name):
	try:
		with open('{}/urls.json'.format(name), 'r+') as f:
			print '{}/urls.json already exists'.format(name)
			print
	except IOError:
		with open('{}/urls.json'.format(name), 'w') as f:
			print '{}/urls.json created'.format(name)
			print


def get_username():
	try:
		user_name = str(raw_input('Public Username (without "@"):  '))
		print
		if len(user_name) > 0:
			global username
			username = user_name
			return user_name
		else:
			print 'Please check your input'
			return get_username
	except:
		print 'Please check your input'
		return get_username()


def get_id(username):
	url = 'https://www.instagram.com/{}?__a=1'.format(username)
	r = requests.get(url)
	if str(r) != '<Response [200]>':
		print 'Please check your input'
		print
		return get_username_id()
	else:
		user_id = json.loads(r.text)['user']['id']
		make_sure_path_exists(username)
		make_sure_json_exists(username)
		return user_id


def get_username_id():
	try:
		return get_id(get_username())
	except:
		return get_username_id()
		

def get_timeline_media(url):
	cookie = str(raw_input('Cookie:  '))
	print
	cookie_dict = {}
	for i in cookie.split('; '):
	    if len(i.split('=')) == 2:
	            cookie_dict[i.split('=')[0]] = i.split('=')[1]
	    if len(i.split('=')) == 3:
	            cookie_dict[i.split('=')[0]] = i.split('=')[1]+'='+i.split('=')[2]
	r = requests.get(url,cookies=cookie_dict)
	if str(r) != '<Response [200]>':
		print 'Please check your input'
		print
		return get_username_media()
	else:
		return json.loads(r.text)


timeline_media_url = 'https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables={"id":"%s","first":10000}'%(get_username_id())
data = get_timeline_media(timeline_media_url)


urls = []
for i in data['data']['user']['edge_owner_to_timeline_media']['edges']:
	urls.append(i['node']['display_url'])

with open('{}/urls.json'.format(username), 'r+') as f:
	try:
		old_urls = json.load(f)
	except ValueError:
		old_urls = []
	updated = json.dumps(list(set(urls+old_urls)))
	f.write(updated)

new_urls = [x for x in urls if x not in old_urls]

print 'Downloading Images...'
print

for idx, i in enumerate(new_urls):
	img = Image.open(StringIO(requests.get(i).content))
	img.save('{}/{}'.format(username, i.split('/')[-1]))
	progress(idx+1, len(new_urls))

print
print
print 'Done'
