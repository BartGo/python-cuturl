exit

# git clone https://github.com/bartgo/bottle-cuturl bottle-cuturl.git
# cd bottle-cuturl.git

pip install --upgrade pip
pip install --upgrade vex

rm --recursive --force env
rm --recursive --force build
rm --recursive --force downloads
                              
mkdir env
mkdir build
mkdir downloads

virtualenv env --no-site-packages --verbose

# --- before bootstrapping
#
# vex --path env pip install --upgrade bottle
# vex --path env pip install --upgrade peewee
# vex --path env pip freeze  > requirements.txt
# echo "-r requirements.txt" > requirements-dev.txt
# echo ""                   >> requirements-dev.txt 
# vex --path env pip install --upgrade cookiecutter
# vex --path env pip freeze >> requirements-dev.txt

vex --path env pip install --download downloads -r requirements-dev.txt
vex --path env pip install --no-index --find-links=/x/bottle-cuturl.git/downloads -r requirements-dev.txt

vex --path env cookiecutter https://github.com/avelino/cookiecutter-bottle.git
