
set -euo pipefail
IFS=$'\n\t'

VENV_USED=1
VENV_NAME=${PWD##*/}

rm --recursive --force lib

pip install --user --upgrade pip pew virtualenv vex bumpversion tox pylint wheel setuptools

if [ $VENV_USED -eq 1 ]; then
  pew rm     $VENV_NAME
  pew new -d $VENV_NAME
  pew in     $VENV_NAME pip install --upgrade --requirement requirements-dev.txt
  echo "pew in $VENV_NAME python -B manage.py runserver --debug True" > devrun.sh
else
  mkdir -p lib
  pip install --upgrade --requirement requirements-dev.txt --target lib
  echo "python -B manage.py runserver --debug True" > devrun.sh
fi

echo ""
echo "To start the app: devrun.sh"
echo ""

sleep 3
