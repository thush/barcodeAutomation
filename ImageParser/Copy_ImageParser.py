#!/usr/bin/python
from __future__ import print_function

import os

from scipy import misc
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread


class Copy_ImageParser:
    def __init__(self):
        self.__members = 'Test'
        self.__path = ''

    def __readImage(self, path, name):
        # image = cv2.imread(os.path.join(path, name))
        image = misc.imread(os.path.join(path, name), flatten=1)
        return image

    # print type(im)
    # def rgb2gray(rgb):
    #     return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

    def parseImage(self, path, name):
        img1 == self.__readImage(path ,name)  # misc.imread(os.path.join( "DATAMATRIX_barcode.bmp"), flatten=1

        # data = np.zeros((4736,), dtype=np.uint8)
        img = np.asarray(img1, dtype=np.uint8)
        h = img1.shape[0]
        w = img1.shape[1]
        ww = 0
        if (w % 8):
            ww = w  # 8 + 1
        else:
            ww = w  # 8
        print('ww -> ', ww)
        print('size', h, w)
        print('now size', img.size)
        # data = np.zeros((4736,), dtype=np.uint8)
        data = np.zeros((h * ww,), dtype=np.uint8)
        wall = np.ones((128, 37), dtype=np.uint8) * 255
        # data2 = np.zeros((4736,), dtype=np.uint8)
        print('img', img.size)
        t = 7
        dataElement = 0
        temp = 0xff

        for row in img:
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
            if (t > 0):
                data[dataElement] = temp
                # print(format(data[dataElement], '02x'), ' ', dataElement, ' ', k, ' ', l)
                t = 7
                temp = 0xff
                dataElement = dataElement + 1
        x = 0
        y = 0
        img3 = data.reshape(h, ww)
        wall[x:x + img3.shape[0], y:y + img3.shape[1]] = img3
        wall = wall.reshape(4736, )
        print('List size...', len(wall))
        return wall
