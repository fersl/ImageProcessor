import util as util
import filters.histogram_functions as hf
from filters.intensity_filters import *

##### CONSTANTS #####
c_log = 1
c_gamma = 1
c_gamma_power = 0.3


def list_img(list):
    for i in list:
        print(str(list.index(i)) + ' - ' + i.get("name"))


if __name__ == '__main__':
    im_list = util.load_images()
    list_img(im_list)

    im1 = im_list[25]  # breast x-ray
    im2 = im_list[11]  # fourrier spectrum
    im3 = im_list[27]  # fractured spine
    im4 = im_list[1]   # aerial image

    # negative(im1, 1)
    # logarithm(im2, c_log, 1)
    # gamma(im3, c_gamma, c_gamma_power, 1)

    # aux = np.unpackbits(im1)
    # aux