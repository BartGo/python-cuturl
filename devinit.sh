
set -euo pipefail
IFS=$'\n\t'

VENV_USED=1
VENV_NAME=${PWD##*/}

rm --recursive --force downloads
rm --recursive --force lib
mkdir -p downloads
mkdir -p lib

pip install --upgrade pip pew virtualenv vex bumpversion tox pylint

if [ $VENV_USED -eq 1 ]; then
  pew rm     $VENV_NAME
  pew new -d $VENV_NAME
  # pew in   $VENV_NAME pip install --download downloads --requirement requirements-dev.txt
  pew in     $VENV_NAME pip install --upgrade --requirement requirements-dev.txt
  #                                 --no-index --find-links=downloads 
  echo "pew in $VENV_NAME python -B manage.py runserver --debug True" > devrun.sh
else
  echo "python -B manage.py runserver --debug True" > devrun.sh
fi

echo ""
echo "To start the app: devrun.sh"
echo ""
