import numpy as np
import matplotlib.pyplot as plt
from math import *


def negative(im_dic, plot):
    im = im_dic.get('im_obj')

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            pixel = 255 - im[i][j]
            im[i][j] = pixel

    if plot:
        plt.imshow(im, cmap='gray')
        plt.show()
    return im


def logarithm(im_dic, c, plot):
    im = im_dic.get('im_obj')

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            pixel = c * log(1 + im[i][j])
            im[i][j] = pixel

    if plot:
        plt.imshow(im, cmap='gray')
        plt.show()
    return im


def gamma(im_dic, c, g, plot):
    im = im_dic.get('im_obj')

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            pixel = (255/(256 ** g)) * ((1 + im[i][j]) ** g)
            # pixel = c * (im[i][j] ** g)
            im[i][j] = pixel

    if plot:
        plt.imshow(im, cmap='gray')
        plt.show()
    return im

def contrast_stretching(im_dic, points, plot):
    im = im_dic.get('im_obj')


def bit_slicing(im_dic, layer, plot):
    im = im_dic.get('im_obj')



def bit_layers(im_dic):
    im = im_dic.get('im_obj')
