from ccdproc import CCDData
import sys
import glob
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.axes_grid1 import make_axes_locatable

class ShowFits(object):

    def __init__(self):
        self.args = sys.argv

        try:
            if '*' not in self.args[1]:
                self.file_list = [arg for arg in self.args if '.fits' in arg]
                # self.keywords = [a]
            else:
                self.file_list = glob.glob(self.args[1])

            if self.file_list == []:
                print('Error')

        except IndexError:
            pass


    def __call__(self, *args, **kwargs):
        for image in self.file_list:
            ccd = CCDData.read(image, unit='adu')

            zlow, zhigh = self.__set_limits(ccd=ccd)


            fig, ax = plt.subplots()
            fig.canvas.set_window_title(image)


            manager = plt.get_current_fig_manager()
            manager.window.showMaximized()

            im = ax.imshow(ccd.data, clim=(zlow, zhigh))
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('right', size="2%", pad=0.05)
            fig.colorbar(im, cax=cax)
            plt.tight_layout()
            plt.show()

    def __set_limits(self, ccd):
        z1 = np.mean(ccd.data) - 0.5 * np.std(ccd.data)
        z2 = np.median(ccd.data) + np.std(ccd.data)

        return z1, z2


def show_fits():
    show__fits = ShowFits()
    show__fits()
