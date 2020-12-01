from PIL import Image
import  numpy as np
import matplotlib.pyplot as plt
import  time

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


'''i = Image.open('./DATAMATRIX_barcode.bmp')
iar = np.array(i)
threshold(iar)


fig = plt.figure(),
ax1 = plt.subplot2grid( ( 8,8), (0,0), rowspan=4, colspan=3 )

ax1.imshow(iar)
plt.show()
'''


i = Image.open('BHi.bmp')
iar = np.array(i)
# i2 = Image.open('images/numbers/y0.4.png')
# iar2 = np.array(i2)
# i3 = Image.open('images/numbers/y0.5.png')
# iar3 = np.array(i3)
# i4 = Image.open('images/sentdex.png')
# iar4 = np.array(i4)

iar = threshold(iar)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax1.imshow(iar)

plt.show()