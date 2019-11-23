import imageio
import os
import cmath
import matplotlib.pyplot as plt
import numpy as np


def load_images():
    im_path_list = os.listdir('./images/images_grayscale/')
    imgs = []

    for im_name in im_path_list:
        if im_name.endswith('.tif'):
            imgs.append({
                "name": im_name,
                "im_obj": imageio.imread('images/images_grayscale/' + im_name)
            })
    return imgs


def load_images_rgb():
    im_path_list = os.listdir('./images/images_rgb/')
    imgs = []

    for im_name in im_path_list:
        if im_name.endswith('.tif'):
            imgs.append({
                "name": im_name,
                "im_obj": imageio.imread('images/images_rgb/' + im_name)
            })
    return imgs



def normalize(im):
    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            result[i][j] = im[i][j] / 255
            # print(result[i][j])
    return result



def normalize_rgb(im):
    height, width, channels = im.shape
    result = np.ndarray((height, width, channels), np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                result[i][j][k] = im[i][j][k] / 255
    return result


def show_image(im):
    plt.imshow(im, cmap='gray')
    plt.show()



def compare_gray(im1, im2):
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(im1, cmap='gray')
    axarr[1].imshow(im2, cmap='gray')
    plt.show()



def compare_rgb(im1, im2):
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(im1)
    axarr[1].imshow(im2)
    plt.show()



def im_subtraction_gs(im1, im2, plot):
    result = im1 - im2

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result



def im_subtraction_rgb(im1, im2, plot):
    result = im1 - im2

    if plot:
        plt.imshow(result)
        plt.show()
    return result

def to_polar(im):
    height, width = im.shape
    result = np.ndarray((height, width), np.uint8)

    for i in range(height):
        for j in range(width):
            print(cmath.polar(im[i][j]))
            # result[i][j] = cmath.polar(im[i][j])

    # return result