# import serial
# import time
#
#
# ACK = 0x06
# NAK = 0x25
# STx = 0x02
# ETx = 0x03
#
# EINK_SET_CONFIG = 0x22
# EINK_BLKN_CHUNK = 0x23
# EINK_DISPLAY = 0x24
# EINK_CLEAR = 0x25
# EINK_GET_CONFIG = 0x26
#
# ZOOM_LEVEL = 0x01
# CHUNK_SIZE = 0x32
# TIME_OUT = 0x05
#
# dataStarted = False
# dataBuf = ""
# messageComplete = False
#
# ser = serial.Serial('COM8', 9600)
# ser.flushInput()
#
#
# # ========================
#
# def setupSerial(baudRate, serialPortName):
#
#     global  serialPort
#
#     serialPort = serial.Serial(port= serialPortName, baudrate = baudRate, timeout=0, rtscts=True)
#
#     print("Serial port " + serialPortName + " opened  Baudrate " + str(baudRate))
#
# # ==================
#
# def recvFromArduino():
#     global STx, ETx
#
#     ck = ""
#     x = "z"  # any value that is not an end- or startMarker
#     byteCount = -1  # to allow for the fact that the last increment will be one too many
#
#     # wait for the start character
#     while ord(x) != STx:
#         x = ser.read()
#
#     # save data until the end CRC is found
#     while ord(x) != ETx:
#         ck = ck + x
#         x = ser.read()
#         byteCount += 1
#
#     # save the end CRC byte
#     ck = ck + x
#
#     returnData = []
#     returnData.append(ord(ck[1]))
#     returnData.append(decodeBytes(ck))
#     print "RETURNDATA " + str(returnData[0])
#
#     return (returnData)
#
#
# # ==================
#
# def decodeBytes(ck):
#
#
#
# #Test Runner to Test
#
# setupSerial(9600 , "COM8")
# count = 0
#
# while True:
#     # check and Print
#     print ("Time %s  Reply %s" %(time.time() ))
