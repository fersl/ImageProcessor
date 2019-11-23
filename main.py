import numpy as np
from run_grayscale import *
from run_colors import *
import util as util
import matplotlib.pyplot as plt
import filters.histogram_functions as hf
import compression.lzw as lzw
import compression.run_length as rl
from filters.color_conversion import *
from filters.frequency_filters import *
from PIL import Image


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

    im = Image.open('images/compression/benchmark.bmp')
    im = np.array(im)
    # print(p.shape)


    # rl.compress_rl(im)
    rl.decompress_rl('benchmark.bin')
    # lzw.compress_lzw(im)
    # lzw.decompress_lzw('teste.bmp')
    # lzw.bin2dec('1001111110000000100')



