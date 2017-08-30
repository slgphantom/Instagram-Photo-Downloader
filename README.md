# Instagram-Photo-Downloader
`instagram_photo_download.py`
A python script to dump all photos within a public instagram account, no login required, using instagram's private api.
<br>
`instagram_photo_download_with_cookies.py`
A python script to dump all photos within a private/public instagram account that you are following, cookies required, using instagram's private api.
<br>
<br>

## Installation
`pip install -r requirements.txt`
<br>
<br>


## Usage
### public instagram account
- open terminal, type `instagram_photo_download.py`
- type a public telegram username in the python input promt (without '@'), e.g. `google`
- a new directory with the username input (e.g. `google`) will be generated if it is not already there
- all photos owned by that user will then be saved in this directory
- a `urls.json` will aslo be generated/updated in the directory with all the urls (of the photos) downloaded
<br>

### private instagram account
- open terminal, type `instagram_photo_download_with_cookies.py`
- type a public telegram username in the python input promt (without '@'), e.g. `google`
- type your cookies in the python input promt , e.g. `mid=WQEPRFEGRSGSRC_Cq4e_C...ds_user_id=24567370`
- a new directory with the username input (e.g. `google`) will be generated if it is not already there
- all photos owned by that user will then be saved in this directory
- a `urls.json` will aslo be generated/updated in the directory with all the urls (of the photos) downloaded
<br>

## Notice
- only support instagram public account
- video and sidecar (except for the first one) will not be downloaded, will be supported in the future
- remove the `urls.json` if you want to download the photos again
<br>

## Cookies
- to get the cookies, login https://www.instagram.com/ 
- open developer tools of the browser
- open the traffic tab
- click on any urls contains '?query_id='
- check the requests header
- cookies is there
<br>

## Known Issue
- when you enter the cookies in terminal, it may exceed the limit of 255 character, which will led to the failure of the script
- to solve this, you can use the default python idle to run the script
- however, using the default idle may cause the process bar print on new lines instead of updating the same line
