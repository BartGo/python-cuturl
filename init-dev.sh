
# --- cloning
# cd /x/
# git clone https://github.com/bartgo/bottle-cuturl MYREPO
# cd MYREPO

MY_VENV="ve-bc"

echo "***"
echo "Creating virtual environment $MY_VENV"
echo "***"
echo ""

echo "Upgrade tools..."
# Consider: pip install --user --upgrade *
pip install --upgrade pip
pip install --upgrade virtualenv
pip install --upgrade pew

echo "Purge and recreate virtual environment..."
pew rm     $MY_VENV
pew new -d $MY_VENV
echo ""
echo "***"
echo "New virtualenv $MY_VENV will be using:"
pew in     $MY_VENV python --version
pew in     $MY_VENV pip --version
echo "***"
echo ""

echo "***"
echo "Download requirements and keep downloaded packages..."
echo "***"
echo ""
mkdir -p downloads

# FIX: below has some issues on cmd.exe (starts with a wrong path to txt files) while working fine with Git bash
pew in $MY_VENV pip install --download downloads -r requirements-dev.txt
pew in $MY_VENV pip install --upgrade --no-index --find-links=downloads -r requirements-dev.txt

echo ""
echo "PipDepTree for $MY_VENV:"
pew in $MY_VENV pipdeptree
echo ""

echo "***"
echo "Installing external components (non-Python)..."
echo "In case you do not want to / can not use curl you can use:"
echo "  pew in $MY_VENV python nonpip-dl.py"
echo "***"
echo ""

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

echo ""
echo "***"
echo "pew in $MY_VENV python manage.py runserver --debug True" > pew-manage.sh
echo "pew in $MY_VENV bumpversion patch"                       > pew-bump.sh
echo "pew workon $MY_VENV"                                     > pew-shell.sh
echo "All done."
echo "To start the app: pew-manage.sh"
echo "Shell:            pew-shell.sh"
echo "Bump version:     pew-bump.sh"
echo "To run (command): pew in $MY_VENV (command)"
echo "***"
echo ""