import numpy
from scipy import misc
import numpy as np
import scipy
import scipy.misc
import matplotlib.pyplot as plt
from PIL import ImageOps


f = misc.face()
misc.imsave('296_128.bmp', f) # uses the Image module (PIL)

# im_inverted = ImageOps.invert(f)
im_inverted = numpy.invert(f)

plt.imshow(im_inverted)
plt.show()


#
# from scipy import misc
# face = misc.face()
# misc.imsave('face.png', face) # First we need to create the PNG file
#
# face = misc.imread('face.png')
# type(face)
# print(face.shape,'  ' , face.dtype)
#
# face.tofile('face.raw') # Create raw file
# face_from_raw = np.fromfile('face.raw', dtype=np.uint8)
# face_from_raw.shape
#
# face_from_raw.shape = (768, 1024, 3)
# face_memmap = np.memmap('face.raw', dtype=np.uint8, shape=(768, 1024, 3))
#
# for i in range(10):
#     im = np.random.randint(0, 256, 10000).reshape((100, 100))
#     misc.imsave('random_%02d.png' % i, im)
# from glob import glob
# filelist = glob('random*.png')
# filelist.sort()
