import numpy as np
import matplotlib.pyplot as plt

def show_hist(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    data = im.copy().flatten()
    plt.hist(data, 256)
    plt.show()


# def eq_hist(im):
#     if isinstance(im, dict):
#         img = im.get('im_obj')
#
#
