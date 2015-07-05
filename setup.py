from setuptools import setup, find_packages

# ---
"""Download external components (non-Python)
"""

import sys
sys.path.append("lib")

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
            if chunk:  # filter out keep-alive new chunks
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
    shutil.rmtree("app/assets/jquery", True)
    shutil.os.mkdir("app/assets/jquery")
    shutil.os.mkdir("app/assets/jquery/js")
    download_file("http://code.jquery.com/jquery-1.11.3.min.js")
    shutil.move("jquery-1.11.3.min.js", "app/assets/jquery/js/jquery-1.11.3.min.js")

if True:
    shutil.rmtree("app/assets/skeletoncss", True)
    download_file("https://github.com/dhg/Skeleton/releases/download/2.0.4/Skeleton-2.0.4.zip")
    unzip_file("Skeleton-2.0.4.zip", ".")
    os.remove("Skeleton-2.0.4.zip")
    shutil.move("Skeleton-2.0.4", "app/assets/skeletoncss")

print "*** Done"
print

# ---

__appname__ = "Bottle-Cuturl"
__description__ = "A simple URL Shortener"
__version__ = "0.0.1"
__repository__ = "http://github.com/bartgo/bottle-cuturl"

with open('README.rst') as readme:
    setup(
        name=__appname__,
        version=__version__,
        description=__description__,
        long_description=readme.read(),
        platforms="any",
        author="BartGo",
        author_email="bartoszgo@poczta.onet.pl",
        license="MIT",
        keywords="url shortener python bottle",
        url=__repository__,
        packages=find_packages(),
        package_data={'app': ["views/*.*",
                              "assets/skeletoncss/index.html",
                              "assets/skeletoncss/css/*.*",
                              "assets/skeletoncss/images/*.*",
                              "assets/jquery/js/*.*"]},
        install_requires=[
            'Beaker==1.7.0',
            'bottle==0.12.8',
            'bottle-sqlalchemy==0.4.2',
            'click==4.0',
            # 'fake-factory==0.5.2',
            'importlib==1.0.3',  # needs to be added explicitely for OpenShift
            # 'Jinja2==2.7.3',
            # 'MarkupSafe==0.23',
            'requests==2.7.0',
            'SQLAlchemy==1.0.6',
            'python-slugify==1.1.2',
            'Unidecode==0.4.18'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
