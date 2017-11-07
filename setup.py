from distutils.core import setup

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
