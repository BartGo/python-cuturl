
rm --recursive --force env
rm --recursive --force app/static/assets/jquery
rm --recursive --force app/static/assets/skeletoncss


virtualenv env --no-site-packages


mkdir --verbose downloads
mkdir --verbose app/static/assets/jquery
mkdir --verbose app/static/assets/jquery/js

curl -LO "https://github.com/dhg/Skeleton/releases/download/2.0.4/Skeleton-2.0.4.zip" \
     -LO "http://code.jquery.com/jquery-1.11.3.min.js"

mv Skeleton-2.0.4.zip downloads
unzip -q downloads/Skeleton-2.0.4.zip
rm downloads/Skeleton-2.0.4.zip

mv --verbose Skeleton-2.0.4       app/static/assets/skeletoncss
mv --verbose jquery-1.11.3.min.js app/static/assets/jquery/js/jquery-1.11.3.min.js

vex --path env pip install -r requirements.txt
