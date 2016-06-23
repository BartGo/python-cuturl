
set -euo pipefail
IFS=$'\n\t'

mkdir -p downloads
pip install  --user --upgrade -r requirements-global.txt
pip download -d downloads     -r requirements-dev.txt
rm --recursive --force lib
mkdir -p lib

virtualenv --clear -q -p python2.7 --no-pip --no-wheel --no-setuptools ./.cvenv
virtualenv --clear -q -p python2.7                                     ./.dvenv

./.dvenv/bin/pip install -r requirements-dev.txt -f downloads --no-index -U
             pip install -r requirements.txt     -f downloads --no-index -U -t lib

echo "./.cvenv/bin/python -B manage.py runserver" > devrun.sh
echo "./.dvenv/bin/python -B manage.py alltests"  > devtests.sh
echo "printf '\nRunning feature tests\n\n'"      >> devtests.sh
echo "./.dvenv/bin/behave"                       >> devtests.sh
echo "./.dvenv/bin/pylint --output-format=parseable app/ alembic/ features/ tests/ *.py" > devlint.sh

chmod +x ./devrun.sh
chmod +x ./devtests.sh
chmod +x ./devlint.sh
chmod +x ./manage.py

./devtests.sh

echo ""
echo "To start: ./devrun.sh"
echo "To test:  ./devtests.sh"
echo "To lint:  ./devlint.sh"
echo ""

sleep 3
