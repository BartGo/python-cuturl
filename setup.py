from setuptools import setup, find_packages

__appname__ = "Bottle-Cuturl"
__description__ = "A simple URL Shortener"
__version__ = "0.0.18" 
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
            'Beaker==1.7.0',
            #'bottle==0.12.8',
            'bottle-sqlalchemy==0.4.2',
            'cherrypy==3.8.0',
            'click==5.1',
            "configparser>=3.3.0",
	        "crashreporter==1.07",
            # 'importlib==1.0.3',  # may need to be added explicitely for OpenShift
            "logbook==0.10.1",
            "psycopg2", # if you want to use peewee with postgresql
            'requests==2.7.0',
            #'SQLAlchemy==1.0.8',
            'alembic==0.8.2',
            'Mako==0.1.2',
            # --
            'python-slugify==1.1.3',
            'Unidecode==0.4.18'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
