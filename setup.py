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
            'Beaker==1.8.0',
            'bottle==0.12.10',
            'bottle-sqlalchemy==0.4.3',
            'cherrypy==8.1.2',
            'click==6.6',
            "configparser==3.5.0",
            #"crashreporter", # somehow does not like setuptools==21.0.0
            "fake-factory==0.7.2",
            "funcsigs==1.0.2",
            # "importlib",  # may need to be added explicitely for OpenShift; is it OK for Python 3??
            "ipaddress==1.0.17", # may need to be added explicitely for Drone.io, probably due to fake-factory
            "logbook==1.0.0",
            #"psycopg2", # if you want to use peewee with postgresql; note that it cannot be directly used with pypy
            'requests==2.11.1',
            'SQLAlchemy==1.1.1',
            'alembic==0.8.8',
            'Mako==1.0.4',
            'python-slugify==1.2.1',
            'Unidecode==0.4.19',
            'WebTest==2.0.23'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
