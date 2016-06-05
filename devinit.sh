
set -euo pipefail
IFS=$'\n\t'

VENV_USED=1
VENV_FIRST_INIT=1

VENV_NAME=$( echo ${PWD##*/} | sed 's/[^a-z]*//g' ) # venv name is the current folder name (only lowercase characters)

rm --recursive --force lib

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
  pip install --upgrade --requirement requirements-dev.txt --target lib
  echo "python -B manage.py alltests" > devtests.sh
  echo "python -B manage.py runserver" > devrun.sh
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
