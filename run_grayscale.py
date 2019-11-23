from filters.intensity_filters import *
from filters.spatial_filters import *
import imageio
import util as util

##########   INTENSITY FILTERS   ##########

def run_negative():
    im = imageio.imread('images/images_grayscale/breast_digital_Xray.tif')
    result = get_negative(im)
    util.compare_gray(im, result)


def run_brightness(const):
    im = imageio.imread('images/images_grayscale/fractured_spine.tif')
    result = get_brightness(im, const)
    util.compare_gray(im, result)


def run_log():
    im = imageio.imread('images/images_grayscale/DFT_no_log.tif')
    result = get_logarithm(im)
    util.compare_gray(im, result)


def run_gamma(c, exp):
    #intensity_ramp, fractured_spine, washed_out_aerial
    im = imageio.imread('images/images_grayscale/fractured_spine.tif')
    result = get_gamma(im, c, exp)
    util.compare_gray(im, result)


def run_piecewise(point1, point2):
    im = imageio.imread('images/images_grayscale/polen_low_contrast.tif')
    result = get_piecewise(im, point1, point2)
    util.compare_gray(im, result)


def run_tsh(const):
    im = imageio.imread('images/images_grayscale/hubble_original.tif')
    result = get_thresholding(im, const)
    util.compare_gray(im, result)


def run_bitslice_d(layer):
    im = imageio.imread('images/images_grayscale/100-dollars.tif')
    result = bit_slicing_d(im, layer)
    util.compare_gray(im, result[layer])


def run_bitslice_c(layer):
    im = imageio.imread('images/images_grayscale/100-dollars.tif')
    result = bit_slicing_c(im, layer)
    util.compare_gray(im, result[layer])



##########   SPATIAL FILTERS    ##########

def run_average():      # escolher tamanho da vizinhança?
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_average(im)
    util.compare_gray(im, result)


def run_wmean(matrix):
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_weighted_average(im, matrix)
    util.compare_gray(im, result)


def run_gmean():
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_geometric_mean(im)
    util.compare_gray(im, result)

def run_convolution(matrix):
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_convolution(im, matrix)
    util.compare_gray(im, result)


def run_median():
    im = imageio.imread('images/images_grayscale/ckt_board_saltpep_prob_pt05.tif')
    result = get_median(im)
    util.compare_gray(im, result)


def run_min():
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_min(im)
    util.compare_gray(im, result)


def run_max():
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_max(im)
    util.compare_gray(im, result)


def run_midpoint():
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_midpoint(im)
    util.compare_gray(im, result)


def run_hmean():
    im = imageio.imread('images/images_grayscale/1test_pattern_blurring_orig00.tif')
    result = get_harmonic_mean(im)
    util.compare_gray(im, result)


def run_chmean(const):
    im = imageio.imread('images/images_grayscale/test_pattern_blurring_orig.tif')
    result = get_counterharmonic_mean(im, const)
    util.compare_gray(im, result)


def run_laplacian():    # acho que precisa de mais alguns passos na função
    im = imageio.imread('images/images_grayscale/blurry_moon.tif')
    result = apply_laplacian(im)
    util.compare_gray(im, result)


def run_sobel():
    im = imageio.imread('images/images_grayscale/contact_lens_original.tif')
    result = get_sobel(im)
    util.compare_gray(im, result)


def run_highboost(const):
    im = imageio.imread('images/images_grayscale/100-dollars.tif')  # mudar img
    result = apply_highboost(im, const)
    util.compare_gray(im, result)
