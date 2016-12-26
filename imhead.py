#!/usr/bin/python2.7
"""Utility to read headers from FITS files

This tool is intended to be used from a terminal in order to have easy access
FITS headers.

If the arguments are only one image it will print the full header like IRAF's imheader
would do with the option longheader+ (l+). If you parse more than one image at a time it
will print the image name and the value of the keyword OBJECT

Mode of Use:
    imhead.py image.fits
    imhead.py *.fits

"""
from astropy.io import fits
import sys
import glob

__author__ = 'Simon Torres'
__date__ = '2016-12-26'
__version__ = "1.0"
__email__ = "storres@ctio.noao.edu"


class ImageHeader(object):

    def __init__(self):
        """Defines the environment for getting keyword's values

        Also performs some checks on the validity of the input
        """
        self.args = sys.argv
        # print self.args
        try:
            if '*' not in self.args[1]:
                # if the program is called from a terminal
                self.file_list = [arg for arg in self.args if '.fits' in arg]
                # self.keywords = [arg for arg in self.args[1:] if '.fits' not in arg]
            else:
                # if the program is called from pycharm
                self.file_list = glob.glob(self.args[1])
                # self.keywords = self.args[2:]
            if self.file_list == []:
                print('Error: No images to get header')
                self.usage_exit()
            # if self.keywords == []:
                # print('Error: No keywords requested')
                # self.usage_exit()
        except IndexError:
            self.usage_exit()

    def __call__(self):
        """Get header and print results"""
        for image in self.file_list:
            # image_info = "%s" % image
            try:
                header = fits.getheader(image)
                # print(header.keys)
                if len(self.file_list) == 1:
                    for keyword in header:
                        print '{:8}= {:30} / {:47}'.format(keyword, header[keyword], header.comments[keyword])
                else:
                    print('{:35} {:15}'.format(image, header['OBJECT']))
            except IOError:
                print("Image %s is corrupt or doesn't have a header" % image)
            # except KeyError as err:
                # image_info += "\t<KeyError %s>" % key.upper()
            # print image_info

    @staticmethod
    def usage_exit():
        """Print usage and exit"""
        sys.exit('\nUsage: \n\timhead.py image.fits\n\timhead.py *fits')


if __name__ == '__main__':
    imhead = ImageHeader()
    imhead()

# Atmospheric Pressure [hPS] at start of exposur