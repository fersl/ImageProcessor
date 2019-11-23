import numpy as np
import math

def get_negative_rgb(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                result[i][j][k] = 255 - im[i][j][k]
    return result



def get_brightness_rgb(im, c):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)


    for i in range(height):
        for j in range(width):
            for k in range(channels):
                aux = (c * im[i][j][k])
                if aux > 255: aux = 255
                result[i][j][k] = aux
    return result



def get_logarithm_rgb(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                aux = im[i][j][k] / 255
                result[i][j][k] = 255 * math.log((1 + aux), 2)
    return result



def get_gamma_rgb(im, g):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                # pixel = c * (im[i][j] ** g)
                result[i][j][k] = (255 / (256 ** g)) * ((1 + im[i][j][k]) ** g)
    return result



def get_thresholding_rgb(im, c):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                if im[i][j][k] >= c:
                    result[i][j][k] = 255
                else:
                    result[i][j][k] = 0
    return result



def get_sepia(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            r = im[i][j][0]
            g = im[i][j][1]
            b = im[i][j][2]

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255: tr = 255
            if tg > 255: tg = 255
            if tb > 255: tb = 255

            result[i][j] = [tr, tg, tb]
    return result



def get_grayscale(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    height, width, channels = im.shape
    result = np.ndarray((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            r = im[i][j][0]
            g = im[i][j][1]
            b = im[i][j][1]

            result[i][j] = (0.3 * r) + (0.59 * g) + (0.11 * b)

    return result

