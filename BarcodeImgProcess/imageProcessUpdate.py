import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
	
	

def parseImage(path):
    img1 = imread("barcode.gif")
    gray = rgb2gray(img1)
    #data = np.zeros((4736,), dtype=np.uint8)
    img = np.asarray(gray, dtype=np.uint8)
    h = gray.shape[0]
    w = gray.shape[1]
    ww = 0
    if (w % 8):
        ww = w // 8 + 1
    else:
        ww = w // 8
    print('ww -> ',ww)
    print('size',h,w)
    print('now size',img.size)
    # data = np.zeros((4736,), dtype=np.uint8)
    data = np.zeros((h*ww ,), dtype=np.uint8)
    wall = np.ones((128, 37), dtype=np.uint8) * 255
    # data2 = np.zeros((4736,), dtype=np.uint8)
    print('img', img.size )
    t = 7
    dataElement = 0
    temp = 0xff
    # Loop in rows in gray image:
    # for row in gray:
    for row in img:
         for element in row:
            if element == 0:
                temp = temp & ~(1 << t)
            if (t > 0):
                t = t - 1
            else:
                data[dataElement] = temp
                #print(format(data[dataElement], '02x'), ' ',dataElement,' ',k,' ',l)
                t = 7
                temp = 0xff
                dataElement = dataElement + 1
         if(t > 0):
             data[dataElement] = temp
             #print(format(data[dataElement], '02x'), ' ', dataElement, ' ', k, ' ', l)
             t = 7
             temp = 0xff
             dataElement = dataElement + 1
    x = 0
    y = 0
    img3 = data.reshape(h,ww)
    wall[x:x + img3.shape[0], y:y + img3.shape[1]] = img3
    wall = wall.reshape(4736,)
        # print('List size...', len(data))
    return wall