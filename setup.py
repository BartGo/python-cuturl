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
            'cherrypy==18.6.0',
            'click==7.1.2',
            "faker==8.0.0",
            "flask==1.1.2",
            "flask_sqlalchemy==2.5.1",
            "funcsigs==1.0.2",
            "logbook==1.5.3",
            #"psycopg2==2.8.6",
            'requests==2.25.1',
            'sqlalchemy==1.4.7',
            'alembic==1.5.8',
            'mako==1.1.4',
            'python-slugify==4.0.1',
            'unidecode==1.2.0'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
