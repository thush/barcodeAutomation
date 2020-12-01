import numpy as np
import matplotlib.pyplot as plt
import cv2


np.random.seed(19680801)

image = cv2.imread('xx1.jpg')
image2 = cv2.imread('testX.bmp')
plt.axis("on")
plt.imshow(image)
plt.imshow(image2)

plt.show()

# with cbook.get_sample_data('ada.png') as image_file:
#     image = plt.imread(image_file)
#
# fig, ax = plt.subplots()
# ax.imshow(image)
# ax.axis('off')  # clear x-axis and y-axis
#
#
# # And another image
#
# w, h = 512, 512
#
# with cbook.get_sample_data('ct.raw.gz') as datafile:
#     s = datafile.read()
# A = np.frombuffer(s, np.uint16).astype(float).reshape((w, h))
# A /= A.max()
#
# fig, ax = plt.subplots()
# extent = (0, 25, 0, 25)
# im = ax.imshow(A, cmap=plt.cm.hot, origin='upper', extent=extent)
#
# markers = [(15.9, 14.5), (16.8, 15)]
# x, y = zip(*markers)
# ax.plot(x, y, 'o')
#
# ax.set_title('CT density')
# plt.show()
#