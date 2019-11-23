from filters.intensity_filters_color import *
from filters.chroma_key import *
import imageio
import util as util
import matplotlib.pyplot as plt
from PIL import Image

##########   INTENSITY FILTERS   ##########

def run_negative_color():
    im = imageio.imread('images/images_rgb/lenna_RGB.tif')
    result = get_negative_rgb(im)
    util.compare_rgb(im, result)


def run_brightness_color(const):
    im = imageio.imread('images/images_rgb/lenna_RGB.tif')
    result = get_brightness_rgb(im, const)
    util.compare_rgb(im, result)


def run_log_color():
    im = imageio.imread('images/images_rgb/strawberries_fullcolor.tif')
    result = get_logarithm_rgb(im)
    util.compare_rgb(im, result)


def run_gamma_color(const):
    im = imageio.imread('images/images_rgb/strawberries_fullcolor.tif')
    result = get_gamma_rgb(im, const)
    util.compare_rgb(im, result)


def run_tsh_color(const):
    im = imageio.imread('images/images_rgb/strawberries_fullcolor.tif')
    result = get_thresholding_rgb(im, const)
    util.compare_rgb(im, result)


def run_sepia():
    im = imageio.imread('images/images_rgb/lenna_RGB.tif')
    result = get_sepia(im)
    util.compare_rgb(im, result)


def run_grayscale():
    im = imageio.imread('images/images_rgb/lenna_RGB.tif')
    result = get_grayscale(im)
    util.compare_rgb(im, result)


def run_chroma():
    im = Image.open('images/chroma_key/shia2.png')
    bg = imageio.imread('images/chroma_key/back2.png')
    print(bg.shape)

    cut_img(im)
    cut_im = imageio.imread('images/chroma_key/cut_im.png')
    print(cut_im.shape)
    result = add_background(cut_im, bg)

    plt.imshow(result)
    plt.show()