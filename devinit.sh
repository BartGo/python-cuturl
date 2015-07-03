# --- cloning
# git clone https://github.com/bartgo/bottle-cuturl MYREPO
# cd MYREPO

# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

VENV_USED=0
VENV_NAME="bottle-cuturl"

# Consider: pip install --user --upgrade *
#pip install --upgrade pip
#pip install --upgrade bumpversion

if [ $VENV_USED -eq 1 ]; then
  pip install --upgrade virtualenv
  pip install --upgrade pew
  pew rm     $VENV_NAME
  pew new -d $VENV_NAME
fi

rm --recursive --force downloads
rm --recursive --force lib
mkdir -p downloads
mkdir -p lib

pip install --download downloads -r requirements-dev.txt
pip install --upgrade --no-index --find-links=downloads -r requirements-dev.txt --target lib

python nonpip-dl.py

if [ $VENV_USED -eq 1 ]; then
  echo "pew in $VENV_NAME python -B manage.py runserver --debug True" > devrun.sh
else
  echo "python -B manage.py runserver --debug True" > devrun.sh
fi
echo ""
echo "To start the app: devrun.sh"
echo ""
