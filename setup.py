# installation: pip install ago

from setuptools import setup

setup( 
    name = 'argparse2',
    version = '0.0.1',
    description = 'argparse2: command-line parsing library',
    keywords = 'argparse2 argparse command line parser parsing',
    long_description = open('readme.rst').read(),

    author = 'Russell Ballestrini',
    author_email = 'russell@ballestrini.net',
    url = 'https://github.com/russellballestrini/argparse2',

    platforms = ['All'],
    license = 'Python Software Foundation License',

    py_modules = ['argparse2'],
    include_package_data = True,
)

# setup keyword args: http://peak.telecommunity.com/DevCenter/setuptools

# built and uploaded to pypi with this:
# python setup.py sdist bdist_egg register upload
