import imageio
import os
import matplotlib.pyplot as plt


def load_images():
    im_path_list = os.listdir('./images/')
    imgs = []

    for im_name in im_path_list:
        imgs.append({
            "name": im_name,
            "im_obj": imageio.imread('images/' + im_name)
        })
    return imgs


def show_image(im):
    plt.imshow(im, cmap='gray')
    plt.show()


# def compare_im(im1, im2):
#     subplot the two imgs