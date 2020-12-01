#!/usr/bin/python
from __future__ import print_function

import numpy as np
from scipy import misc
from binascii import hexlify
import os
import matplotlib.image as mpimg
from binascii import hexlify



def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def __readImage(path, name):
    image = misc.imread(os.path.join(path, name), flatten=1)
    return image


def parseImage():
    # img = __readImage()
    img = mpimg.imread('64_64.bmp')
    gray = rgb2gray(img)
    # plt.imshow(img1)

    img1 = np.asarray(gray, dtype=np.uint8)
    h = gray.shape[0]
    w = gray.shape[1]
    ww = 0
    if (w % 8):
        ww = w // 8 + 1
    else:
        ww = w // 8
    print('ww -> ',ww)
    print('size',h,w)
    print('now size',img1.size)
    # data = np.zeros((4736,), dtype=np.uint8)
    data = np.zeros((h*ww ,), dtype=np.uint8)
    wall = np.ones((296, 16), dtype=np.uint8) * 255

    # data2 = np.zeros((4736,), dtype=np.uint8)
    print('img', img1.size )
    t = 7
    dataElement = 0
    temp = 0xff
    # Loop in rows in gray image:
    # for row in gray:
    #printImg(imgs)
    k = 0
    l = 0
    for row in img1:
         for element in row:
            if element == 0:
                temp = temp & ~(1 << t)
            if (t > 0):
                t = t - 1
            else:
                data[dataElement] = temp
                # print(format(data[dataElement], '02x'), ' ',dataElement,' ',k,' ',l)
                t = 7
                temp = 0xff
                dataElement = dataElement + 1
            l = l +1
         if((t > 0) & (t != 7)):
             data[dataElement] = temp
             # print(format(data[dataElement], '02x'), ' ->', dataElement, ' ', k, ' ', l)
             t = 7
             temp = 0xff
             dataElement = dataElement + 1
         k = k + 1
    x = 0
    y = 0
    img3 = data.reshape(h,ww)
    # printImg(img3)
    wall[x:x + img3.shape[0], y:y + img3.shape[1]] = img3
    wall = wall.reshape(4736,)
    print('List size...', len(wall))

    for j in wall:
        print(format(j, '02x'), end=" ")
    print('    ')


    return wall




parseImage()