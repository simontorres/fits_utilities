from astropy.io import fits
from ccdproc import CCDData
import glob
import os
import re


PATH = '/user/simon/development/soar/goodman_pipeline/goodman_pipeline/data/ref_comp'

keywords = {
    'SLIT': {'0.45" long slit': '0.45_LONG_SLIT'},
    'GRATING': {'SYZY_400':'400_SYZY',
                'SYZY_600-OLD':'600_SYZY_OLD',
                'SYZY_930':'930_SYZY',
                'RALC_1200-BLUE':'1200_RALC_BLUE'},

    'WAVMODE': 'wavmode',
}


def update_keywords(path):
    for _file in glob.glob(os.path.join(path, "*.fits")):
        ccd = CCDData.read(_file, unit='adu')
        print(_file)

        for key in keywords.keys():
            old_value = ccd.header[key]
            if key == 'WAVMODE':
                ccd.header[key] = re.sub(' ', '_', ccd.header[key]).upper()
            else:
                if ccd.header[key] in keywords[key].keys():
                    ccd.header[key] = keywords[key][ccd.header[key]]
            print("replaced {} with {}".format(old_value, ccd.header[key]))
        ccd.write(_file, overwrite=True)



if __name__ == '__main__':
    update_keywords(path=PATH)