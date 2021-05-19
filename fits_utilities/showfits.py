import argparse
import sys
import glob
import goodman_pipeline
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import re

from astropy.visualization import ZScaleInterval
from ccdproc import CCDData
from mpl_toolkits.axes_grid1 import make_axes_locatable


class ShowFits(object):

    def __init__(self):
        self.args = self.get_args()
        self.log = self.__get_logger()
        self.scale = ZScaleInterval()
        self.wcs = goodman_pipeline.wcs.WCS()

        try:
            if len(self.args.files) == 1:
                if os.path.isfile(self.args.files[0]):
                    self.file_list = self.args.files
                elif '*' in self.args.files[0]:
                    self.file_list = glob.glob(self.args.files[0])
            elif len(self.args.files) > 1:
                self.file_list = [file for file in self.args.files if os.path.isfile(file) and '.fits' in file]

            else:
                self.log.error('Unable to obtain files.')

        except IndexError as error:
            self.log.error(str(error))

    def __call__(self, *args, **kwargs):
        for file_name in self.file_list:
            ccd = CCDData.read(file_name, unit='adu')



            if self.args.style == 'light':
                plt.style.use('default')
            elif self.args.style == 'dark':
                plt.style.use('dark_background')
            else:
                plt.style.use('dark_background')


            fig, ax = plt.subplots(figsize=(16, 9))
            fig.canvas.set_window_title(file_name)
            ax.set_title(file_name)
            if ccd.header['NAXIS'] == 2:
                zlow, zhigh = self.scale.get_limits(ccd.data)
                im = ax.imshow(ccd.data, cmap=self.args.cmap, clim=(zlow, zhigh))
                divider = make_axes_locatable(ax)
                cax = divider.append_axes('right', size="3%", pad=0.05)
                fig.colorbar(im, cax=cax)
            elif ccd.header['NAXIS'] == 1:

                wav, intens = self.wcs.read(ccd=ccd)

                ax.plot(wav, intens)
                ax.set_ylabel('Intensity')
                ax.set_xlabel('Wavelength')
            plt.tight_layout()
            plt.show()

    def __get_logger(self):

        if self.args.debug:
            log_format = '[%(asctime)s][%(levelname)8s]: %(message)s ' \
                         '[%(module)s.%(funcName)s:%(lineno)d]'
            logging_level = logging.DEBUG
        else:
            log_format = '[%(asctime)s][%(levelname).1s]: %(message)s'
            logging_level = logging.INFO

        date_format = '%H:%M:%S'

        # formatter = logging.Formatter(fmt=log_format,
        #                               datefmt=date_format)

        logging.basicConfig(level=logging_level,
                            format=log_format,
                            datefmt=date_format)

        log = logging.getLogger(__name__)
        return log

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('files',
                            nargs='+',
                            help="File name or pattern to filter files")

        parser.add_argument('--color-map',
                            action='store',
                            default='viridis',
                            type=str,
                            dest='cmap',
                            choices=['gray', 'viridis', 'gray_inverted'],
                            help='Color map to use')

        parser.add_argument('--style',
                            action='store',
                            default='dark',
                            type=str,
                            dest='style',
                            choices=['dark', 'light'],
                            help='Visual style to use')
        parser.add_argument('--debug',
                            action='store_true',
                            dest='debug',
                            help='Debug messages')

        args = parser.parse_args()
        if 'inverted' in args.cmap:
            args.cmap = re.sub('_inverted', '_r', args.cmap)
        return args


def show_fits():
    show__fits = ShowFits()
    show__fits()


if __name__ == '__main__':
    show_fits()
