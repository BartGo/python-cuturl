#!/bin/bash

set -e -u -o pipefail
IFS=$'\n\t'

python -m pip install --user --upgrade --requirement requirements-global.txt
python -m virtualenv --clear --quiet ./env 
python -m virtualenv --clear --quiet ./dnv 

if [ "$OSTYPE" == "msys" ] ; then
  PYVE="Scripts"
else
  PYVE="bin"
fi

./dnv/$PYVE/pip install --upgrade --requirement requirements-dev.txt
./env/$PYVE/pip install --upgrade --requirement requirements.txt                                      


echo "./env/$PYVE/python -B manage.py unittests" >  devtests.sh
echo "printf '\nRunning feature tests\n\n'"      >> devtests.sh
echo "./dnv/$PYVE/behave"                        >> devtests.sh
echo "./dnv/$PYVE/pylint --output-format=parseable app/ alembic/ features/ tests/ *.py" > devlint.sh
echo "export DATABASE_URL=""sqlite:///data//sqlite.db""" >  devrun.sh
#export DATABASE_URL=""postgresql+psycopg2://cuturl:cuturl@localhost:5432/python-cuturl""
chmod +x ./devrun.sh
chmod +x ./devtests.sh
chmod +x ./devlint.sh
chmod +x ./devucl.sh
chmod +x ./manage.py

./devrun.sh
./devtests.sh

echo "./env/$PYVE/python -B manage.py runserver" >> devrun.sh

echo ""
echo "To start: ./devrun.sh"
echo "To test:  ./devtests.sh"
echo "To lint:  ./devlint.sh"
echo ""
sleep 3
