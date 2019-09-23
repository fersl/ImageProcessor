import imageio
import os
import matplotlib.pyplot as plt


def load_images():
    im_path_list = os.listdir('./images/')
    imgs = []

    for im_name in im_path_list:
        if im_name.endswith('.tif'):
            imgs.append({
                "name": im_name,
                "im_obj": imageio.imread('images/' + im_name)
            })
    return imgs


def show_image(im):
    plt.imshow(im, cmap='gray')
    plt.show()


def compare_gray(im1, im2):
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(im1, cmap='gray')
    axarr[1].imshow(im2, cmap='gray')
    plt.show()



def im_subtraction_gs(im1, im2, plot):
    result = im1 - im2

    if plot:
        plt.imshow(result, cmap='gray')
        plt.show()
    return result



def im_subtraction_color(im1, im2, plot):
    result = im1 - im2

    if plot:
        plt.imshow(result)
        plt.show()
    return result