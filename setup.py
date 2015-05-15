from setuptools import setup, find_packages, Extension
setup(
    name = "Bottle-Cuturl",
    version = "0.0.1a1",
    packages = find_packages(),

    install_requires = [
        'Beaker==1.7.0',
        'bottle==0.12.8',
        'bottle-sqlalchemy==0.4.2',
        'click==4.0',
        'fake-factory==0.5.0',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        'requests==2.7.0',
        'SQLAlchemy==1.0.4'
    ],

    author = "BartGo",
    description = "Bottle-Cuturl",
    license = "MIT",
    keywords = "url shortener python bottle",
    url = "http://github.com/bartgo/bottle-cuturl",

)

