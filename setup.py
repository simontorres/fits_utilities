import os

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open


here = os.path.abspath(os.path.dirname(__file__))


def create_version_py(packagename, version, source_dir='.'):
    package_dir = os.path.join(source_dir, packagename)
    version_py = os.path.join(package_dir, 'version.py')

    version_str = "# This is an automatic generated file please do not edit\n" \
                  "__version__ = '{:s}'".format(version)

    with open(version_py, 'w') as f:
        f.write(version_str)


# read content from README.md
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()


# Get configuration information from setup.cfg
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
conf = ConfigParser()


# conf.read([os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')])
conf.read([os.path.join(os.path.dirname(__file__), 'setup.cfg')])
metadata = dict(conf.items('metadata'))

PACKAGENAME = metadata['package_name']

VERSION = metadata['version']

LICENSE = metadata['license']

DESCRIPTION = metadata['description']

LONG_DESCRIPTION = long_description

LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

AUTHOR = metadata['author']

AUTHOR_EMAIL = metadata['author_email']

INSTALL_REQUIRES = metadata['install_requires'].split()

# freezes version information in version.py
create_version_py(PACKAGENAME, VERSION)

setup(
    name='fitsutils',
    version='1.0b1',
    packages=['utils'],
    package_dir={'utils': 'utils'},
    scripts=['bin/imhead', 'bin/hselect'],
    test_suite="utils.tests.test_imports",
    url='https://github.com/simontorres/fitsUtilities',
    license='GNU/GPL',
    author='Simon Torres R.',
    author_email='storres@ctio.noao.edu',
    description='Fits Utilities To read FITS images header'
)
