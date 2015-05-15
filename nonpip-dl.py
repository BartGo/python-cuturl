"""Download external components (non-Python)
"""

import requests
import zipfile
import os
import shutil

# http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
def download_file(url):
    """Download a file"""
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename
    
# http://stackoverflow.com/questions/9431918/extracting-zip-file-contents-to-specific-directory-in-python-2-7    
def unzip_file(file_in, file_out):
    """Unzip a file"""
    fh = open(file_in, 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        outpath = file_out
        z.extract(name, outpath)
    fh.close()
   
print "*** Downloading non-Python components"

if True:
    shutil.rmtree("app/static/assets/jquery", True)
    shutil.os.mkdir("app/static/assets/jquery")
    shutil.os.mkdir("app/static/assets/jquery/js")
    download_file("http://code.jquery.com/jquery-1.11.3.min.js")
    shutil.move("jquery-1.11.3.min.js", "app/static/assets/jquery/js/jquery-1.11.3.min.js")

if True:
    shutil.rmtree("app/static/assets/bootstrap", True)
    download_file("https://github.com/twbs/bootstrap/releases/download/v3.3.4/bootstrap-3.3.4-dist.zip")
    unzip_file("bootstrap-3.3.4-dist.zip", ".")
    os.remove("bootstrap-3.3.4-dist.zip")
    shutil.move("bootstrap-3.3.4-dist", "app/static/assets/bootstrap")

print "*** Done"
print
