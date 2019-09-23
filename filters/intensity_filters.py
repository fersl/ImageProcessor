import numpy as np
import matplotlib.pyplot as plt
from math import *


def get_negative(im, plot):
    if isinstance(im, dict):
        im = im.get('im_obj')

    result = np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8)

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            result[i][j] = 255 - im[i][j]

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result



def get_brightness(im, c, plot):
    if isinstance(im, dict):
        im = im.get('im_obj')

    result = np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8)

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            aux = (c * im[i][j])
            print(aux)
            if aux > 255: aux = 255
            result[i][j] = aux

    if plot:
        plt.imshow(im, cmap='gray')
        plt.show()
    return result



def get_logarithm(im, c, plot):
    if isinstance(im, dict):
        im = im.get('im_obj')

    result = np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8)


    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            result[i][j] = c * log(1 + im[i][j])

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result



def get_gamma(im, c, g, plot):
    if isinstance(im, dict):
        im = im.get('im_obj')

    result = np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8)

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            # pixel = c * (im[i][j] ** g)
            result[i][j] = (255 / (256 ** g)) * ((1 + im[i][j]) ** g)

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result



def get_piecewise(im, point1, point2, plot):
    if isinstance(im, dict):
        im = im.get('im_obj')

    result = np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8)

    aux = np.array(range(0, 256), dtype=np.uint8)
    xp = [point1[0], point2[0]]
    fp = [point1[1], point2[1]]

    if np.all(np.diff(xp) > 0):
        aux = np.interp(aux, xp, fp)
    else:
        print('x-coordinates of points must be in increasing order')

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            result[i][j] = np.uint8(aux[im[i][j]])

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result



def get_thresholding(im, c, plot):
    if isinstance(im, dict):
        im = im.get('im_obj')

    result = np.zeros((im.shape[0], im.shape[1]), dtype=np.uint8)

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i][j] >= c:
                result[i][j] = 255
            else:
                result[i][j] = 0

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result




def get_layers(im):     # retorna uma lista com 8 arrays, cada um contendo uma posição de cada byte da img
    # ex: layers[0] contém o bit mais significativo de cada pixel
    if isinstance(im, dict):
        im = im.get('im_obj')
    layers = [np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8) for i in range(8)]

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            byte_str = np.binary_repr(im[i][j], 8)
            for k in range(8):
                layers[k][i][j] = int(byte_str[k])
    return layers



def bit_slicing_c(im, layer, plot):       # deixa apenas 1 bit em cada byte
    # ex: layers[0] mantém o bit menos significativo de cada pixel, os outros recebem 0
    if isinstance(im, dict):
        im = im.get('im_obj')
    layers = [np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8) for i in range(8)]

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            byte_str = np.binary_repr(im[i][j], 8)
            layers[0][i][j] = np.uint8(int('0000000' + byte_str[7], 2))
            layers[1][i][j] = np.uint8(int('000000' + byte_str[6] + '0', 2))
            layers[2][i][j] = np.uint8(int('00000' + byte_str[5] + '00', 2))
            layers[3][i][j] = np.uint8(int('0000' + byte_str[4] + '000', 2))
            layers[4][i][j] = np.uint8(int('000' + byte_str[3] + '0000', 2))
            layers[5][i][j] = np.uint8(int('00' + byte_str[2] + '00000', 2))
            layers[6][i][j] = np.uint8(int('0' + byte_str[1] + '000000', 2))
            layers[7][i][j] = np.uint8(int(byte_str[0] + '0000000', 2))

    if plot:
        plt.imshow(layers[layer], cmap='gray')
        plt.show()
    return layers



def bit_slicing_d(im, layer, plot):    # remove apenas 1 bit em cada byte
    # ex: layers[0] muda o bit menos significativo para 0
    if isinstance(im, dict):
        im = im.get('im_obj')
    layers = [np.ndarray((im.shape[0], im.shape[1]), dtype=np.uint8) for i in range(8)]

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            byte_str = np.binary_repr(im[i][j], 8)
            layers[0][i][j] = np.uint8(int(byte_str[:6] + '0', 2))
            layers[1][i][j] = np.uint8(int(byte_str[:5] + '0' + byte_str[7], 2))
            layers[2][i][j] = np.uint8(int(byte_str[:4] + '0' + byte_str[6:7], 2))
            layers[3][i][j] = np.uint8(int(byte_str[:3] + '0' + byte_str[5:7], 2))
            layers[4][i][j] = np.uint8(int(byte_str[:2] + '0' + byte_str[4:7], 2))
            layers[5][i][j] = np.uint8(int(byte_str[:1] + '0' + byte_str[3:7], 2))
            layers[6][i][j] = np.uint8(int(byte_str[0] + '0' + byte_str[2:7], 2))
            layers[7][i][j] = np.uint8(int('0' + byte_str[1:7], 2))

    if plot:
        plt.imshow(layers[layer], cmap='gray')
        plt.show()
    return layers