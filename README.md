![Fits Utilities](https://github.com/simontorres/fits_utilities/workflows/Fits%20Utilities/badge.svg)
[![Build Status](https://travis-ci.org/simontorres/fitsUtilities.svg?branch=master)](https://travis-ci.org/simontorres/fitsUtilities)
[![Documentation Status](https://readthedocs.org/projects/fitsutilities/badge/?version=latest)](http://fitsutilities.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/73316179.svg)](https://zenodo.org/badge/latestdoi/73316179)


# Fits Utilities
Some tiny tools for handling FITS files

# Install

```shell
pip install fits-utilities
```

## hselect

Utility to read headers from FITS files. It works as Iraf's _hselect_
and _imhead longheader=no_ 

This tool is intended to be used from a terminal in order to have easy
access to them

Mode of Use:

```shell
hselect image.fits keyword1 keyword2 ... keywordN
```

It is also possible to use wildcards:
```shell
hselect *.fits keyword1 keyword2 ... keywordN
```

To have a quick look of what images are:
```shell
hselect *.fits
```

## imhead

Displays full headers

```shell
imhead file_001.fits
```


## showfits

Displays images using matplotlib. For 1D files the x-axis will always show `Wavelength` even if it is pixels.
This is inteded as a quick look tool only

```shell
showfits file_001.fits
```

Or for showing several (one after another)

```shell
showfits *fits
```

# Future plans
I plan to include some other tools (as needed) that should work as in
IRAF, such as:

1. `hedit`
2. `imstat`

If you are interested in one of those let me know.
