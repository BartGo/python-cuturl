from setuptools import setup, find_packages

__version__ = "0.0.1"

with open('README.rst') as readme:
    setup(
        name = "Bottle-Cuturl",
        version = __version__,
        description="A simple URL Shortener",
        long_description=readme.read(),
        platforms = "any",
        author = "BartGo",
        author_email = "bartoszgo@poczta.onet.pl",
        license = "MIT",
        keywords = "url shortener python bottle",
        url = "http://github.com/bartgo/bottle-cuturl",
        packages = find_packages(),
        package_data = {'app' : ["views/*.*",
          "assets/skeletoncss/index.html",
          "assets/skeletoncss/css/*.*",
          "assets/skeletoncss/images/*.*",
          "assets/jquery/js/*.*"]},
        install_requires = [
            'Beaker==1.7.0',
            'bottle==0.12.8',
            'bottle-sqlalchemy==0.4.2',
            'click==4.0',
            'fake-factory==0.5.2',
            'importlib==1.0.3', # needs to be added explicitely for OpenShift
            # 'Jinja2==2.7.3',
            # 'MarkupSafe==0.23',
            'requests==2.7.0',
            'SQLAlchemy==1.0.6'
        ],
        classifiers=(
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Framework :: Bottle',
            'Programming Language :: Python'
        )
    )
