from setuptools import setup, find_packages

__appname__ = "Python-Cuturl"
__description__ = "A simple URL Shortener"
__version__ = "0.0.23" 
__repository__ = "http://github.com/bartgo/python-cuturl"
__tarball__ = "https://github.com/bartgo/python-cuturl/tarball/v" + __version__


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
            'Beaker==1.11.0',
            'bottle==0.12.18',
            'bottle-sqlalchemy==0.4.3',
            'cherrypy==18.5.0',
            'click==7.0',
            "configparser==4.0.2",
            "Faker==3.0.0",
            "funcsigs==1.0.2",
            "logbook==1.5.3",
            "psycopg2==2.8.4",
            'requests==2.22.0',
            'SQLAlchemy==1.3.12',
            'alembic==1.3.2',
            'Mako==1.1.0',
            'python-slugify==4.0.0',
            'Unidecode==1.1.1',
            'WebTest==2.0.33'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
