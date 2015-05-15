# --- how was it cloned

# cd /x/
# git clone https://github.com/bartgo/bottle-cuturl bottle-cuturl.git
# cd bottle-cuturl.git

# --- installing additional python components

# --- note: for pythonanywhere it is better to do pip install --user --upgrade *

pip install --upgrade pip
pip install --upgrade virtualenv
pip install --upgrade vex

rm --recursive --force env
rm --recursive --force build
rm --recursive --force downloads
                              
mkdir env
mkdir build
mkdir downloads

virtualenv env --no-site-packages

vex --path env pip install --download downloads -r requirements-dev.txt
vex --path env pip install --upgrade --no-index --find-links=downloads -r requirements-dev.txt
# vex --path env pip install -r requirements-dev.txt

# --- installing external components (non-Python)

rm --recursive --force app/static/assets/skeletoncss
rm --recursive --force app/static/assets/jquery
mkdir --verbose app/static/assets/jquery
mkdir --verbose app/static/assets/jquery/js

curl -LO "https://github.com/dhg/Skeleton/releases/download/2.0.4/Skeleton-2.0.4.zip" \
     -LO "http://code.jquery.com/jquery-1.11.3.min.js"

# --- in case of problems with curl you can use: vex --path env python nonpip-dl.py
	 
mv Skeleton-2.0.4.zip downloads
unzip -q downloads/Skeleton-2.0.4.zip
rm downloads/Skeleton-2.0.4.zip

mv --verbose Skeleton-2.0.4       app/static/assets/skeletoncss
mv --verbose jquery-1.11.3.min.js app/static/assets/jquery/js/jquery-1.11.3.min.js

exit
