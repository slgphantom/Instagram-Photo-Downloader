# Instagram-Photo-Downloader
A python script to dump all photos within a public instagram account, no login required, using instagram's private api.
<br>
<br>

## Installation
`pip install -r requirements.txt`
<br>
<br>


## Usage
- open terminal, type `instagram_photo_download.py`
- type a public telegram username in the python input promt (without '@'), e.g. `google`
- a new directory with the username input (e.g. `google`) will be generated if it is not already there
- all photos owned by that user will then be saved in this directory
- a `urls.json` will aslo be generated/updated in the directory with all the urls (of the photos) downloaded
<br>

## Notice
- only support instagram public account
- video and sidecar (except for the first one) will not be downloaded, will be supported in the future
- remove the `urls.json` if you want to download the photos again
