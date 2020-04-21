"""Utility to read headers from FITS files

This tool is intended to be used from a terminal in order to have easy access
FITS headers

Mode of Use:
    hselect.py image.fits keyword1 keyword2 ... keywordN
"""
from __future__ import absolute_import

from astropy.io import fits
import sys
import glob

__author__ = 'Simon Torres'
__date__ = '2016-11-09'
__version__ = "1.0"
__email__ = "storres@ctio.noao.edu"


class HeaderSelect(object):

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
                self.keywords = [arg for arg in self.args[1:] if '.fits' not in arg]
            else:
                # if the program is called from pycharm
                self.file_list = glob.glob(self.args[1])
                self.keywords = self.args[2:]
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
            image_info = "%s" % image
            try:
                header = fits.getheader(image)
                if self.keywords == []:
                    dimensions = [header['NAXIS%s' % i] for i in range(1, int(header['NAXIS']) + 1, 1)]
                    image_info += "%s: %s" %(dimensions, header['OBJECT'])
                else:
                    for key in self.keywords:
                        image_info += "\t%s" % header[key]
            except IOError:
                print("Image %s is corrupt or doesn't have a header" % image)
            except KeyError as err:
                image_info += "\t<KeyError %s>" % key.upper()
            print(image_info)

    @staticmethod
    def usage_exit():
        """Print usage and exit"""
        sys.exit('\nUsage: \n\thselect image.fits keyword1 keyword2 ... keywordN')


def header_select():
    hselect = HeaderSelect()
    hselect()