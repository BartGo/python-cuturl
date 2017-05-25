#!/bin/bash

set -e -u -o pipefail
IFS=$'\n\t'

pip install --user --upgrade --requirement requirements-global.txt

virtualenv --clear --quiet ./env # --python=python2.7
virtualenv --clear --quiet ./dnv # --python=python2.7

if [ "$OSTYPE" == "msys" ] ; then
  PYVE="Scripts"
else
  PYVE="bin"
fi
#echo $PYVE

./dnv/$PYVE/pip install --upgrade --requirement requirements-dev.txt
./env/$PYVE/pip install --upgrade --requirement requirements.txt

echo "./env/$PYVE/python -B manage.py runserver" >  devrun.sh
echo "./env/$PYVE/python -B manage.py unittests" >  devtests.sh
echo "printf '\nRunning feature tests\n\n'"      >> devtests.sh
echo "./dnv/$PYVE/behave"                        >> devtests.sh
echo "./dnv/$PYVE/pylint --output-format=parseable app/ alembic/ features/ tests/ *.py" > devlint.sh

chmod +x ./devrun.sh
chmod +x ./devtests.sh
chmod +x ./devlint.sh
chmod +x ./devucl.sh
chmod +x ./manage.py

./devtests.sh

echo ""
echo "To start: ./devrun.sh"
echo "To test:  ./devtests.sh"
echo "To lint:  ./devlint.sh"
echo ""

sleep 3
