#!/usr/bin/python
from __future__ import print_function

import os
import matplotlib.pyplot as mpimg
import numpy as np
from scipy import misc
from itertools import islice
# import matplotlib.pyplot as plt

class ImageParser:
    def __init__(self):
        self.__members = 'Test'
        self.__path = ''

    def __rgb2gray(self,rgb):
        return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


    def __readImage(self, path, name):
        print('Relative Path ', path)
        image = mpimg.imread(os.path.join(path, name))
        # image = misc.imread(os.path.join(path, name), flatten=1)

        print('read success..')

        return image



    def parseImage(self, path, name):
        img = self.__readImage(path, name)
        gray = self.__rgb2gray(img)

        img1 = np.asarray(gray, dtype=np.uint8)
        h = gray.shape[0]
        w = gray.shape[1]
        ww = 0
        if (w % 8):
            ww = w // 8 + 1
        else:
            ww = w // 8
        print('ww -> ', ww)
        print('size', h, w)
        print('New Re-sized ', img1.size)
        data = np.zeros((4736,), dtype=np.uint8)

        data = np.zeros((h * ww,), dtype=np.uint8)
        wall = np.ones((296, 16), dtype=np.uint8) * 255
        # data2 = np.zeros((4736,), dtype=np.uint8)
        print('img', img1.size)
        t = 7
        dataElement = 0
        # temp = 0xFF
        temp = np.uint8(255)
        print('temp....',type(temp))

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
                    temp = 0xFF
                    dataElement = dataElement + 1
                l = l + 1
            if ((t > 0) & (t != 7)):
                data[dataElement] = temp
                # print(format(data[dataElement], '02x'), ' ->', dataElement, ' ', k, ' ', l)
                t = 7
                temp = 0xFF
                dataElement = dataElement + 1
            k = k + 1
        x = 0
        y = 0
        img3 = data.reshape(h, ww)
        # printImg(img3)
        wall[x:x + img3.shape[0], y:y + img3.shape[1]] = img3
        wall = wall.reshape(4736, )
        print('List size...', len(wall))

        # for j in wall:
        #     print(format(j, '02x'), end=" ")


        return wall


    # function called for Testing..
    # parseImage('','')

    # def parseImage(self, path, name):
    #     img = self.__readImage(path, name)  # misc.imread(os.path.join( "DATAMATRIX_barcode.bmp"), flatten=1
    #     # data = np.zeros((4736,), dtype=np.uint8)
    #     data = np.ones((4736,), dtype=np.uint8)*255
    #
    #     t = 7
    #     dataElement = 0
    #     temp = 0x00
    #     # Loop in rows in image:
    #
    #     i = 0
    #     w = img.shape[1]
    #
    #     for row in img:
    #         for x in range(row.size):
    #             # print('range', x, " - " , row.size)
    #             element = row[x]
    #
    #             if element == 0:
    #                 temp = temp | (0 << t)
    #             if (t > 0) and (x != row.size-1):
    #                 t = t - 1
    #             elif (t == 0) or (x == row.size-1):
    #
    #                 data[dataElement+i*16] = temp
    #                 t = 7
    #                 temp = 0x00
    #                 dataElement = dataElement + 1
    #
    #         i = i +1
    #
    #     for i in data:
    #         print('0x',hexlify(i),',')
    #
    #     print('temp', type(temp))
    #     return data

