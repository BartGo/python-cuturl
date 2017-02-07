
set -euo pipefail
IFS=$'\n\t'

# *** note that both lib and downloads are present in .gitignore
rm --recursive --force lib
#rm --recursive --force downloads
mkdir --parents downloads
mkdir --parents lib
pip install  --user --upgrade --requirement requirements-global.txt
pip download -d downloads     --requirement requirements-dev.txt

virtualenv --clear --quiet -p python2.7 --no-pip --no-wheel --no-setuptools ./.cvenv
virtualenv --clear --quiet -p python2.7                                     ./.dvenv

./.dvenv/bin/pip install --requirement requirements-dev.txt --find-links downloads --no-index --upgrade
             pip install --requirement requirements.txt     --find-links downloads --no-index --upgrade --target lib

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
