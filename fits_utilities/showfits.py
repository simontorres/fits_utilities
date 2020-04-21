import argparse
import sys
import glob
import matplotlib.pyplot as plt
import numpy as np
import re

from ccdproc import CCDData
from mpl_toolkits.axes_grid1 import make_axes_locatable


class ShowFits(object):

    def __init__(self):
        self.args = self.get_args()

        try:
            if '*' not in self.args.files:
                self.file_list = [arg for arg in self.args.files if '.fits' in arg]
                # self.keywords = [a]
            else:
                self.file_list = glob.glob(self.args.files)

            if self.file_list == []:
                print('Error')

        except IndexError:
            pass

    def __call__(self, *args, **kwargs):
        for file_name in self.file_list:
            ccd = CCDData.read(file_name, unit='adu')

            zlow, zhigh = self.__set_limits(ccd=ccd)

            if self.args.style == 'light':
                plt.style.use('default')
            elif self.args.style == 'dark':
                plt.style.use('dark_background')
            else:
                plt.style.use('dark_background')


            fig, ax = plt.subplots(figsize=(16, 9))
            fig.canvas.set_window_title(file_name)
            ax.set_title(file_name)
            im = ax.imshow(ccd.data, cmap=self.args.cmap, clim=(zlow, zhigh))
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('right', size="3%", pad=0.05)
            fig.colorbar(im, cax=cax)
            plt.tight_layout()
            plt.show()

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('files', help="File name or pattern to filter files")

        parser.add_argument('--color-map',
                            action='store',
                            default='viridis',
                            type=str, dest='cmap',
                            choices=['gray', 'viridis', 'gray_inverted'],
                            help='Color map to use')

        parser.add_argument('--style',
                            action='store',
                            default='dark',
                            type=str, dest='style',
                            choices=['dark', 'light'],
                            help='Visual style to use')

        args = parser.parse_args()
        if 'inverted' in args.cmap:
            args.cmap = re.sub('_inverted', '_r', args.cmap)
        return args

    @staticmethod
    def __set_limits(ccd):
        z1 = np.mean(ccd.data) - 0.5 * np.std(ccd.data)
        z2 = np.median(ccd.data) + np.std(ccd.data)

        return z1, z2


def show_fits():
    show__fits = ShowFits()
    show__fits()
