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
            'cherrypy==18.6.1',
            'click==8.0.1',
            "faker==8.13.2",
            "flask==2.0.1",
            "flask_sqlalchemy==2.5.1",
            "funcsigs==1.0.2",
            "logbook==1.5.3",
            #"psycopg2==x.x.x",
            'requests==2.31.0',
            'sqlalchemy==1.4.23',
            'alembic==1.7.3',
            'mako==1.1.5',
            'python-slugify==5.0.2',
            'unidecode==1.3.2'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
