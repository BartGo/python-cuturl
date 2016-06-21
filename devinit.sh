
set -euo pipefail
IFS=$'\n\t'

VENV_USED=0
VENV_FIRST_INIT=1

VENV_NAME=$( echo ${PWD##*/} | sed 's/[^a-z]*//g' ) # venv name is the current folder name (only lowercase characters)

rm --recursive --force lib
rm --recursive --force downloads

pip install --user --upgrade --requirement requirements-dev-base.txt # TODO: sure for global?

if [ $VENV_USED -eq 1 ]; then
  if [ $VENV_FIRST_INIT -eq 0 ]; then
    pew wipeenv $VENV_NAME
    pew rm     $VENV_NAME
  fi
  pew new -d  $VENV_NAME
  pew in      $VENV_NAME pip install --upgrade --requirement requirements-dev.txt
  echo "pew in $VENV_NAME python -B manage.py runserver --debug True" > devrun.sh
  echo "pew in $VENV_NAME python -B manage.py alltests" > devtests.sh
  echo "pew in $VENV_NAME pylint --output-format=parseable app/ alembic/ features/ tests/ *.py" > devlint.sh
  # useful for fabric
  chmod +x devrun.sh
  chmod +x devtests.sh
  chmod +x devlint.sh 
else
  mkdir -p lib
  mkdir -p downloads
  pew new -d clean # nothing installed inside
  pip install --download downloads --requirement requirements-dev.txt # will be made obsolete by pip download
  pip install --no-index --find-links=downloads --upgrade --requirement requirements-dev.txt --target lib # some will be wheels, not sure if it is OK?
  echo "pew in clean python -B manage.py alltests" > devtests.sh
  echo "pew in clean python -B manage.py runserver" > devrun.sh
  # useful for fabric 
  chmod +x ./devtests.sh
  chmod +x ./devrun.sh
fi

chmod +x manage.py
./devtests.sh

echo ""
echo "To start the app:   devrun.sh"
echo "To rerun all tests: devtests.sh"
echo ""

sleep 3
