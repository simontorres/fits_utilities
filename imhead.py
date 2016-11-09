#!/usr/bin/env python2.7
"""Utility to read headers from FITS files

This tool is intended to be used from a terminal in order to have easy access
to them

Mode of Use:
    imhead.py image.fits keyword1 keyword2 ... keywordN
"""
from astropy.io import fits
import sys
import glob

__author__ = 'Simon Torres'
__date__ = '2016-11-09'
__version__ = "1.0"
__email__ = "storres@ctio.noao.edu"


class ImageHeader(object):

    def __init__(self):
        """Defines the environment for getting keyword's values

        Also performs some checks on the validity of the input
        """
        self.args = sys.argv
        try:
            self.file_list = glob.glob(self.args[1])
            self.keywords = self.args[2:]
            if self.file_list == []:
                print('Error: No images to get header')
                self.usage_exit()
            if self.keywords == []:
                print('Error: No keywords requested')
                self.usage_exit()
        except IndexError:
            self.usage_exit()

    def __call__(self):
        """Get header and print results"""
        for image in self.file_list:
            image_info = "%s\t" % image
            try:
                header = fits.getheader(image)
                for key in self.keywords:
                    image_info += "%s\t" % header[key]
            except IOError:
                print("Image %s is corrupt or doesn't have a header" % image)
            except KeyError as err:
                image_info += "<KeyError %s> \t" % key.upper()
            print image_info

    @staticmethod
    def usage_exit():
        """Print usage and exit"""
        sys.exit('\nUsage: \n\timhead.py image.fits keyword1 keyword2 ... keywordN')


if __name__ == '__main__':
    imhead = ImageHeader()
    imhead()