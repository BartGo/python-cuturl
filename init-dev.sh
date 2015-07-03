# --- cloning
# cd /x/
# git clone https://github.com/bartgo/bottle-cuturl MYREPO
# cd MYREPO

# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

MY_VENV="bottle-cuturl"

echo "Upgrade tools..."

# Consider: pip install --user --upgrade *
pip install --upgrade pip
pip install --upgrade virtualenv
pip install --upgrade pew
pip install --upgrade bumpversion

echo "Purge and recreate virtual environment..."
pew rm     $MY_VENV
pew new -d $MY_VENV
echo ""

rm --recursive --force downloads
rm --recursive --force lib
mkdir -p downloads
mkdir -p lib

pip install --download downloads -r requirements-dev.txt
pip install --upgrade --no-index --find-links=downloads -r requirements-dev.txt --target lib

python nonpip-dl.py

echo "pew in $MY_VENV python manage.py runserver --debug True" > pew-manage.sh
echo "To start the app: pew-manage.sh"
echo "To run (command): pew in $MY_VENV (command)"
echo ""
