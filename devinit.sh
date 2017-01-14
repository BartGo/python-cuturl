
set -euo pipefail
IFS=$'\n\t'

pip install --user --upgrade --requirement requirements-global.txt

virtualenv --clear --quiet --python=python2.7 ./env
virtualenv --clear --quiet --python=python2.7 ./dnv

# TODO: use Scripts for Windows
./dnv/bin/pip install --upgrade --requirement requirements-dev.txt
./env/bin/pip install --upgrade --requirement requirements.txt

echo "./env/bin/python -B manage.py runserver" > devrun.sh
echo "./env/bin/python -B manage.py unittests" > devtests.sh
echo "printf '\nRunning feature tests\n\n'"    >> devtests.sh
echo "./dnv/bin/behave"                        >> devtests.sh
echo "./dnv/bin/pylint --output-format=parseable app/ alembic/ features/ tests/ *.py" > devlint.sh

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
