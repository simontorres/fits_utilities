# Fits Utilities
Some tiny tools for handling FITS files

## imhead.py

Utility to read headers from FITS files

This tool is intended to be used from a terminal in order to have easy
access to them

Mode of Use:

```shell
imhead.py image.fits keyword1 keyword2 ... keywordN
```

It is also possible to use wildcards:
```shell
imhead.py *.fits keyword1 keyword2 ... keywordN
```


# Future plans
I plan to include some other tools (as needed) that should work as in
IRAF, such as:

1. display.py
2. hedit.py
3. imstat.py

If you are interested in one of those let me know.