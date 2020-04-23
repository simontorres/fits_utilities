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
    name=metadata['package_name'],

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=VERSION,

    description=DESCRIPTION,

    long_description=LONG_DESCRIPTION,

    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,

    # The project's main homepage.
    url='https://github.com/simontorres/fits_utilities',

    # Author details
    author=u'Simon Torres R., ',

    author_email='storres@ctio.noao.edu',

    # Choose your license
    license=LICENSE,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',

        'Natural Language :: English',

        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Other',
        'Operating System :: MacOS :: MacOS X',

        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],

    # What does your project relate to?
    keywords='astronomy images',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().

    packages=find_packages(),

    package_dir={'fits_utilities': 'fits_utilities'},



    install_requires=INSTALL_REQUIRES,

    entry_points={
        "console_scripts": [
            "showfits = fits_utilities.showfits:show_fits",
            "hselect = fits_utilities.hselect:header_select",
            "imhead = fits_utilities.imhead:image_header"]},

   )
