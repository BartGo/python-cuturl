from setuptools import setup, find_packages

__appname__ = "Bottle-Cuturl"
__description__ = "A simple URL Shortener"
__version__ = "0.0.22" 
__repository__ = "http://github.com/bartgo/bottle-cuturl"
__tarball__ = "https://github.com/bartgo/bottle-cuturl/tarball/v" + __version__


with open('README.rst') as readme:
    setup(
        name=__appname__,
        version=__version__,
        description=__description__,
        long_description=readme.read(),
        platforms="any",
        author="BartGo",
        author_email="bartoszgo@poczta.onet.pl",
        license="MIT",
        keywords="url shortener python bottle",
        url=__repository__,
        download_url = __tarball__,
        packages=find_packages(),
        package_data={'app': ["views/*.*",
                              "assets/skeletoncss/index.html",
                              "assets/skeletoncss/css/*.*",
                              "assets/skeletoncss/images/*.*",
                              "assets/jquery/js/*.*"]},
        install_requires=[
            'Beaker==1.9.0',
            'bottle==0.12.13',
            'bottle-sqlalchemy==0.4.3',
            'cherrypy==11.0.0',
            'click==6.7',
            "configparser==3.5.0",
            #"crashreporter", # somehow does not like setuptools==21.0.0
            #"fake-factory==0.7.4",
            "Faker==0.7.18",
            "funcsigs==1.0.2",
            # "importlib",  # may need to be added explicitely for OpenShift; is it OK for Python 3??
            "ipaddress==1.0.18", # may need to be added explicitely for Drone.io, probably due to fake-factory
            "logbook==1.1.0",
            #"psycopg2", # if you want to use peewee with postgresql; note that it cannot be directly used with pypy
            'requests==2.18.3',
            'SQLAlchemy==1.1.13',
            'alembic==0.9.4',
            'Mako==1.0.7',
            'python-slugify==1.2.4',
            'Unidecode==0.4.21',
            'WebTest==2.0.28'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
