import numpy as np
import util as util
import filters.histogram_functions as hf
from filters.intensity_filters import *
from filters.spatial_filters import *

##### CONSTANTS #####
c_log = 1
c_brightness = 0.5
c_gamma = 1
c_gamma_power = 0.3
c_laplacian = -1
point_1 = [130, 60]
point_2 = [210, 120]
matrix = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])


def list_img(list):
    for i in list:
        print(str(list.index(i)) + ' - ' + i.get("name"))


if __name__ == '__main__':
    im_list = util.load_images()
    # list_img(im_list)

    im1 = im_list[22].get('im_obj')     # breast x-ray
    im2 = im_list[11].get('im_obj')     # fourrier spectrum
    im3 = im_list[23].get('im_obj')     # fractured spine
    im4 = im_list[1].get('im_obj')      # aerial image
    im5 = im_list[20].get('im_obj')     # contact lens
    im6 = im_list[7].get('im_obj')      # polen
    im7 = im_list[13].get('im_obj')     # teste média
    im8 = im_list[14].get('im_obj')     # blurry moon


    # laplacian(im8, c_laplacian, 1)
    aux = get_median(im6, 0)
    util.compare_gray(im6, aux)
