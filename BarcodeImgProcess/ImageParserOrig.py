#!/usr/bin/python
from __future__ import print_function

import PIL
import os
import time
from itertools import islice
import numpy as np
import serial
from scipy import misc
from scipy import ndimage
from scipy import misc
import urllib2
import cStringIO

def parseImage():
    # img = self.__readImage(self.__path, name)  # misc.imread(os.path.join( "DATAMATRIX_barcode.bmp"), flatten=1
    # data = np.zeros((4736,), dtype=np.uint8)

    img = misc.imread(os.path.join("296_128_Datamatrix.bmp"), flatten=1)



    # data type set to Byte for the full ImageSized= 296*128
    data = np.zeros((4736,), dtype=np.uint8)
    i = 0
    j = 0
    A = np.zeros((296, 128))  # [gray.shape[0]][gray.shape[0]]
    t = 7
    k = 0
    temp = 0
    for eachRow in img:
        for element in eachRow:
            if element != 0:
                temp = temp | (1 << t)
                print(hex(temp), '>')
            # print(A[i][j],t, end=' ')
            if (t > 0):
                t = t - 1
            else:
                data[k] = temp
                # print('<',format(temp, '02x'),' ',format(data[k], '02x'),'--')
                print('<', format(temp, '02x'))
                t = 7
                temp = 0
                k = k + 1
            # print("cell" ,i, j, end=' ')
            j = j + 1
        print('')
        print('<-------------------->')
    # B = A.transpose()
    return data



parseImage()



class ImageParser:
    def __init__(self):
        self.__members = 'Test'
        self.__path = ''

    def setPath(self, path):
        self.__path = path

    def __readImage(self, path, name):
        image = misc.imread(os.path.join(path, name), flatten=1)
        return image
