import numpy as np
from grayscale_functions import *
from color_functions import *
import util as util
import filters.histogram_functions as hf
from filters.color_conversion import *

##### CONSTANTS #####
point_1 = [130, 60]
point_2 = [210, 120]
matrix_wmean = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]])

matrix_conv = np.array([[1, 2, 1],
                        [2, 4, 2],
                        [1, 2, 1]])


def list_img(list):
    for i in list:
        print(str(list.index(i)) + ' - ' + i.get("name"))


#######################################################################
if __name__ == '__main__':
    # im_list = util.load_images()
    # im_list_rgb = util.load_images_rgb()
    # list_img(im_list_rgb)

# Grayscale Intensity Functions:
#     run_negative()
#     run_brightness(2)
#     run_log()
#     run_gamma(1, 0.3)
#     run_piecewise(point_1, point_2)
#     run_tsh()   #need const
#     run_bitslice_c()    #layer
#     run_bitslice_d()    #layer

# Grayscale Spatial Functions:
#     run_average()
#     run_median()
#     run_min()
#     run_max()
#     run_midpoint()
#     run_wmean(matrix_wmean)
#     run_gmean()
#     run_hmean()
#     run_chmean()    #const
#     run_convolution(matrix_conv)
#     run_laplacian()
#     run_sobel()
#     run_highboost() #const

# Color Intensity Functions:
#     color_conversion(insys, outsys, a, b, c)
#     run_negative_color()
#     run_brightness_color(2)  #const
#     run_log_color()
    # run_gamma_color()   #const
    # run_tsh_color()     #const
    # run_sepia()
    # run_chroma()




