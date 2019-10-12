import numpy as np
from math import *
import imageio
from PIL import Image

def cut_img(im):
    output_img = Image.new("RGBA", im.size)

    tola, tolb = 200, 100
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            p = list(im.getpixel((x, y)))
            d = int(sqrt(pow(p[0], 2) + pow((p[1] - 255), 2) + pow(p[2], 2)))
            if d > tola:
                d = 255
            elif (tolb < d):
                p[1] = p[1] - (255 - d)
                d = (d - tolb) * (255 / (tola - tolb))
            else:
                d = 0
            output_img.putpixel((x, y), (p[0], p[1], p[2], int(d)))

    output_img.save('images/chroma_key/cut_im.png', "PNG")



def add_background(cut_im, bg):
    height, width, channels = bg.shape
    result = np.ndarray((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            if cut_im[i][j][3] == 255:
                result[i][j][0] = cut_im[i][j][0]
                result[i][j][1] = cut_im[i][j][1]
                result[i][j][2] = cut_im[i][j][2]
            else:
                result[i][j][0] = bg[i][j][0]
                result[i][j][1] = bg[i][j][1]
                result[i][j][2] = bg[i][j][2]


    # imageio.imwrite('images/chroma_key/result.png', result)
    return result