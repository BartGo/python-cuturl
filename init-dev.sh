# --- how was it cloned

# cd /x/
# git clone https://github.com/bartgo/bottle-cuturl bottle-cuturl.git
# cd bottle-cuturl.git

# --- note: it is better to do pip install --user --upgrade * but PATH change should follow,
# --- please see e.g. "The Path problem" from https://github.com/sashahart/vex/blob/master/README.rst

MY_VENV="env"

echo "Upgrade tools..."
pip install --user --upgrade pip
pip install --user --upgrade virtualenv
pip install --user --upgrade vex
echo "Purge and recreate virtual environment named $MY_VENV..."
vex -r $MY_VENV pip --version
vex -m $MY_VENV python --version
echo "Download requirements and keep downloaded packages..."
mkdir -p downloads
vex $MY_VENV pip install --download downloads -r requirements-dev.txt
vex $MY_VENV pip install --upgrade --no-index --find-links=downloads -r requirements-dev.txt

# --- installing external components (non-Python)
# --- in case you do not want to use curl you can use: vex $MY_VENV python nonpip-dl.py

rm --recursive --force app/assets/skeletoncss
rm --recursive --force app/assets/jquery
mkdir --verbose app/assets/jquery
mkdir --verbose app/assets/jquery/js
curl -LO "https://github.com/dhg/Skeleton/releases/download/2.0.4/Skeleton-2.0.4.zip" \
     -LO "http://code.jquery.com/jquery-1.11.3.min.js"
mv Skeleton-2.0.4.zip downloads
unzip -q downloads/Skeleton-2.0.4.zip
mv --verbose Skeleton-2.0.4       app/assets/skeletoncss
mv --verbose jquery-1.11.3.min.js app/assets/jquery/js/jquery-1.11.3.min.js
rm -f downloads/Skeleton-2.0.4.zip

rm -f run-dev.sh
echo "vex $MY_VENV python manage.py runserver --debug True" > run-dev.sh
echo ""
echo "To run in venv $MY_VENV: run-dev.sh"
echo ""