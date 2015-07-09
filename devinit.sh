
set -euo pipefail
IFS=$'\n\t'

VENV_USED=1
VENV_NAME="bottle-cuturl"

pip install --upgrade pip
pip install --upgrade virtualenv
pip install --upgrade pew
pip install --upgrade vex
pip install --upgrade bumpversion

if [ $VENV_USED -eq 1 ]; then
  pew rm     $VENV_NAME
  pew new -d $VENV_NAME
fi

rm --recursive --force downloads
rm --recursive --force lib
mkdir -p downloads
mkdir -p lib

pew in $VENV_NAME pip install --download downloads -r requirements-dev.txt
pew in $VENV_NAME pip install --upgrade --no-index --find-links=downloads -r requirements-dev.txt

# Disputable, do not install into venv but into ./lib
# pip install --upgrade --no-index --find-links=downloads -r \
#     requirements-dev.txt --target lib

if [ $VENV_USED -eq 1 ]; then
  echo "pew in $VENV_NAME python -B manage.py runserver --debug True" > devrun.sh
else
  echo "python -B manage.py runserver --debug True" > devrun.sh
fi
echo ""
echo "To start the app: devrun.sh"
echo ""
