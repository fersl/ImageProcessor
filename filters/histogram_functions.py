import numpy as np
import matplotlib.pyplot as plt

def show_histogram(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    data = im.copy().flatten()
    plt.hist(data, 256)
    plt.show()



def get_histogram(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    data = im.copy().flatten()
    hist = np.zeros(256)

    for pixel in data:
        hist[pixel] += 1

    return hist


def eq_histogram(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    data = im.copy().flatten()
    hist = np.histogram(data, 256)
    cdf = np.cumsum(hist)

    cdf = 255 * cdf / cdf[-1]

    result = np.interp(image.flatten(), bins[:-1], cdf)
    return result
