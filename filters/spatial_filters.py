import numpy as np
import scipy.stats as sp
from math import *

# def gaussian(x, y, sigma):
#     exponent = ((x**2) + (y**2)) / 2 * (sigma**2)



def neighbours(im, size, i, j):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    mask = np.zeros((size, size), np.uint8)
    mask_limit = size // 2

    for m in range( -mask_limit, mask_limit+1 ):
        for n in range( -mask_limit, mask_limit+1 ):
            if i+m in range(height) and j+n in range(width):
                mask[i+m][j+n] = im[i+m][j+n]
    return mask



def get_neighbours_3(im, i, j):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    mask = np.zeros((3, 3), np.uint8)

    mask[1][1] = im[i][j]
    if i + 1 in range(height):
        mask[0][1] = im[i + 1][j]  # top
    if i - 1 in range(height):
        mask[2][1] = im[i - 1][j]  # bottom
    if j - 1 in range(width):
        mask[1][0] = im[i][j - 1]  # left
    if j + 1 in range(width):
        mask[1][2] = im[i][j + 1]  # right
    if i + 1 in range(height) and j - 1 in range(width):
        mask[0][0] = im[i + 1][j - 1]  # top left
    if i + 1 in range(height) and j + 1 in range(width):
        mask[0][2] = im[i + 1][j + 1]  # top right
    if i - 1 in range(height) and j - 1 in range(width):
        mask[2][0] = im[i - 1][j - 1]  # bottom left
    if i - 1 in range(height) and j + 1 in range(width):
        mask[2][2] = im[i - 1][j + 1]  # bottom right

    return mask



def calculate_counter_harmonic(mask):
    sum_sqr = 0
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += mask[i][j]
            sum_sqr += (mask[i][j]) ** 2
    return (sum_sqr / 9) // (sum / 9)



def get_average (im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = floor(np.mean(mask))
    return result



def get_convolution (im, weight_matrix):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = (mask[0][0] * weight_matrix[2][2] +  # top left
                            mask[0][1] * weight_matrix[2][1] +  # top
                            mask[0][2] * weight_matrix[2][0] +  # top right
                            mask[1][0] * weight_matrix[1][2] +  # left
                            mask[1][1] * weight_matrix[1][1] +  # center
                            mask[1][2] * weight_matrix[1][0] +  # right
                            mask[2][0] * weight_matrix[0][2] +  # bottom left
                            mask[2][1] * weight_matrix[0][1] +  # bottom
                            mask[2][2] * weight_matrix[0][0]    # bottom right
                            ) // 9
    return result



def get_weighted_average (im, weight_matrix):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = (mask[0][0] * weight_matrix[0][0] +
                            mask[0][1] * weight_matrix[0][1] +
                            mask[0][2] * weight_matrix[0][2] +
                            mask[1][0] * weight_matrix[1][0] +
                            mask[1][1] * weight_matrix[1][1] +
                            mask[1][2] * weight_matrix[1][2] +
                            mask[2][0] * weight_matrix[2][0] +
                            mask[2][1] * weight_matrix[2][1] +
                            mask[2][2] * weight_matrix[2][2]) // 9
    return result



def get_median (im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = np.median(mask)
    return result



def get_min(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = np.amin(mask)
    return result



def get_max(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = np.amax(mask)
    return result



def get_midpoint(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = (np.amax(mask) + np.amin(mask)) // 2
    return result



def get_geometric_mean(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = sp.mstats.gmean(mask, axis=None)
    return result



def get_harmonic_mean(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = sp.hmean(mask, axis=None)
    return result



def get_counterharmonic_mean(im, q):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)

            num = 0
            den = 0
            for pixel in np.nditer(mask):
                # print(pixel)
                den += int((pixel ** q))
                num += int((pixel ** (q+1)))

            try: result[i][j] = num // den
            except: result[i][j] = 0
    return result



def get_laplacian (im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            result[i][j] = (mask[0][0] * (-1)) +\
                           (mask[0][1] * (-1)) +\
                           (mask[0][2] * (-1)) +\
                           (mask[1][0] * (-1)) +\
                           (mask[1][1] * 8) +\
                           (mask[1][2] * (-1)) +\
                           (mask[2][0] * (-1)) +\
                           (mask[2][1] * (-1)) +\
                           (mask[2][2] + (-1))
    return result



def apply_laplacian(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)
    laplacian = get_laplacian(im, 0)

    for i in range(height):
        for j in range(width):
            aux = im[i][j] - laplacian[i][j]
            result[i][j] = im[i][j] + aux
    return result



def apply_highboost(im, c):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)
            aux = im[i][j] - floor(np.median(mask))     # change to gaussian blur
            result[i][j] = im[i][j] + (c * aux)
    return result



def get_sobel(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            mask = get_neighbours_3(im, i, j)

            horizontal = mask[0][0] * (-1) +\
                         mask[0][1] * (-2) +\
                         mask[0][2] * (-1) +\
                         mask[1][0] * 0 +\
                         mask[1][1] * 0 +\
                         mask[1][2] * 0 +\
                         mask[2][0] * 1 +\
                         mask[2][1] * 2 +\
                         mask[2][2] * 1

            vertical = mask[0][0] * (-1) +\
                       mask[0][1] * 0 +\
                       mask[0][2] * 1 +\
                       mask[1][0] * (-2) +\
                       mask[1][1] * 0 +\
                       mask[1][2] * 2 +\
                       mask[2][0] * (-1) +\
                       mask[2][1] * 0 +\
                       mask[2][2] * 1

            result[i][j] = np.sqrt((horizontal ** 2) + (vertical ** 2))
    return result