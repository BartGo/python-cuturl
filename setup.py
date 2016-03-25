from setuptools import setup, find_packages

__appname__ = "Bottle-Cuturl"
__description__ = "A simple URL Shortener"
__version__ = "0.0.21" 
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
            'bottle==0.12.9',
            'bottle-sqlalchemy==0.4.3',
            'cherrypy==5.1.0',
            'click==6.4',
            "configparser==3.5.0b2",
            "crashreporter==1.11",
            "fake-factory==0.5.7",
            "importlib==1.0.3",  # may need to be added explicitely for OpenShift
            "ipaddress==1.0.16", # may need to be added explicitely for Drone.io, probably due to fake-factory
            "logbook==0.12.5",
            "psycopg2", # if you want to use peewee with postgresql
            'requests==2.9.1',
            'SQLAlchemy==1.0.12',
            'alembic==0.8.5',
            'Mako==1.0.4',
            'python-slugify==1.2.0',
            'Unidecode==0.4.19'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
