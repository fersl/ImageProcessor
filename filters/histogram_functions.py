import numpy as np
import matplotlib.pyplot as plt

def show_histogram(im):
    if isinstance(im, dict):
        im = im.get('im_obj')

    data = im.copy().flatten()
    plt.hist(data, 256)
    plt.show()



def get_histogram(im, plot):
    if isinstance(im, dict): im = im.get('im_obj')
    hist = np.zeros(256)
    bins = np.arange(256)

    for pixel in np.nditer(im):
        hist[pixel] += 1

    if plot:
        plt.figure()
        plt.bar(bins, hist)
        plt.show()
    return hist



def normalize_histogram(hist):      # hist é um array[256]
    total = np.sum(hist)
    result = np.zeros(256)

    for i in range(256):
        result[i] = hist[i] / total

    return result



def eq_histogram(im, plot):   #testar
    if isinstance(im, dict): im = im.get('im_obj')
    height, width = im.shape
    result_im = np.ndarray((height, width), np.uint8)
    eq_hist = np.zeros(256)
    bins = np.arange(256)

    hist = get_histogram(im, 0)
    cdf = np.cumsum(hist)

    for k in range(256):
        eq_hist[k] = int(cdf[k] * 255 / cdf[255])

    for i in range(height):
        for j in range(width):
            original_intensity = im[i][j]
            result_im[i][j] = eq_hist[original_intensity]
    new_hist = get_histogram(result_im, 0)

    if plot:
        f, axarr = plt.subplots(2, 2)
        axarr[0, 0].imshow(im, cmap='gray')
        axarr[0, 0].set_title('original image')
        axarr[0, 1].imshow(result_im, cmap='gray')
        axarr[0, 1].set_title('equalized image')
        axarr[1, 0].bar(bins, hist)
        axarr[1, 0].set_title('original histogram')
        axarr[1, 1].bar(bins, new_hist)
        axarr[1, 1].set_title('equalized histogram')
        plt.show()




def get_histogram_rgb(im, plot):
    if isinstance(im, dict): im = im.get('im_obj')
    height, width, channels = im.shape
    bins = np.arange(256)

    hist_r = np.zeros(256)
    hist_g = np.zeros(256)
    hist_b = np.zeros(256)

    for i in range(height):
        for j in range(width):
            value_r = im[i][j][0]
            value_g = im[i][j][1]
            value_b = im[i][j][2]

            hist_r[value_r] += 1
            hist_g[value_g] += 1
            hist_b[value_b] += 1

    histograms = [hist_r, hist_g,hist_b]

    if plot:
        plt.figure()
        plt.subplot(131, title='red')
        plt.bar(bins, hist_r)
        plt.subplot(132, title='green')
        plt.bar(bins, hist_g)
        plt.subplot(133, title='blue')
        plt.bar(bins, hist_b)
        plt.show()
    return histograms



def normalize_histogram_rgb(hists):     # hists é um array[3], com os 3 histogramas dos 3 canais de cores
    hist_r = hists[0]
    hist_g = hists[1]
    hist_b = hists[2]

    result_r = np.zeros(256)
    result_g = np.zeros(256)
    result_b = np.zeros(256)
    total = np.sum(hist_r)

    for i in range(256):
        result_r[i] = hist_r[i] / total
        result_g[i] = hist_g[i] / total
        result_b[i] = hist_b[i] / total

    result = [result_r, result_g, result_b]
    return result



#
# def eq_histogram_rgb(im):
#     if isinstance(im, dict): im = im.get('im_obj')
# converter cada pixel rgb para hsi e aplicar equalização na intensidade
