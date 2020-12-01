#!/usr/bin/python
from __future__ import print_function

from CommandPacket import CommandPacket
from DataPacket import DataPacket
import time
import array
from struct import pack
from itertools import islice
from binascii import hexlify

import numpy as np
import serial
from ImageParser import ImageParser


EINK_CLEAR = 0x25
EINK_GET_CONFIG = 0x26

ZOOM_LEVEL = 0x01
CHUNK_SIZE = 0x32
TIME_OUT = 0x05
EINK_SET_CONFIG = 0x22
EINK_BLKN_CHUNK = 0x23
EINK_DISPLAY = 0x24

CMD_ACK = 0x6
CMD_NAK = 0x25
STx = 0x02
ETx = 0x03

CMD_CFG = 0x29

ERROR_ACK = 0
ERROR_NAK = 1
ERROR_CFGOK = 2
ERROR_CFGNOK = 3
ERROR_NCRC = 4

ERROR_CFGOK = 2
ERROR_CFGNOK = 3
ERROR_NCRC = 4

class BarcodeDriver:
    def __init__(self):
        self.__members = 'Test'
        self.__path = ''
        self.ser = ''
        try:
            ser = serial.Serial('COM9', 9600, timeout=10, xonxoff=False, rtscts=False, dsrdtr=False)
        except serial.serialutil.SerialException:
             print ('exception - Can not open device COM9')

    testload = 0

    #COM port iteration set
    def getComPort(self, comport):
        self.__comport =comport

    def setPath(self, path):
        self.__path = path

    def __sendBulkCmd(self, cmd, ser, count):
        cmdPacket = CommandPacket()
        # count.extend(count&0x7F)
        cmdPkt = cmdPacket.createPacket(cmd, (count + 128))

        if (self.__processPacket(ser,0, cmdPkt))== ERROR_ACK:
            pass
        # ser.write(cmdPkt)
        # time.sleep(4.5)


        # Disprelay the pkt for terminal debugging
        cmdPacket.DisplayPacket(cmdPkt)


    def __sendDisplayCmd(self, ser):
        cmdPacket = CommandPacket()
        displayPkt = cmdPacket.createPacket(EINK_DISPLAY, 0)
        ser.write(displayPkt)
        time.sleep(1.0)

        # Display the pkt for terminal debugging
        cmdPacket.DisplayPacket(displayPkt)



    def __sendClearCmd(self, ser ):
        cmdPacket = CommandPacket()
        clearcmdPkt =cmdPacket.createPacket(EINK_CLEAR, 0)
        if (self.__processPacket(ser,0, clearcmdPkt))== ERROR_ACK:
            pass
        # ser.write(clearcmdPkt)

        # Display the pkt for terminal debugging
        cmdPacket.DisplayPacket(clearcmdPkt)



    def __sendSetConfigCmd(self, ser):
        cmdPacket = CommandPacket()
        setConfigPkt = cmdPacket.createPacket(EINK_SET_CONFIG,0)
        ser.write(setConfigPkt)


    def __sendDataChnk(self, arr, ser):
        dataPacket = DataPacket()
        packedData = dataPacket.createDataPacket(arr)
        # ser.write(packedData)

        # Hexlify dataPkt for verification
    #Calling the Processing Response for ACK/NAK
        if (self.__processPacket(ser,0, packedData))== ERROR_ACK:
            pass
    #Check the WrittePacket data after writing-- On Hexlify
        print('Chunks written.....')
        print(hexlify(packedData))



    def __getPixelStream(self, image):
        ps = image[0] < 255
        ps = ps.astype(np.int)
        return ps


    def __splitToChunks(self, it, size):
        it = iter(it)
        return iter(lambda: tuple(islice(it, size)), ())


    def __serialWritePacketStream(self, packetStr, ser):
        lst = list(self.__splitToChunks(packetStr, 128))
        ackFlag = False

        # Do the Clearing of Buffers
        self.__sendClearCmd(ser)

        for i in range(0, len(lst)):
        # for i in range(0, 18):
            self.__sendBulkCmd(EINK_BLKN_CHUNK, ser , i)
            arr = np.array(lst[i])
            self.__sendDataChnk(arr, ser)


            # DataChunk takes 127+CRC or full 128 data Bytes of data????
            # Do the normal houseKeeping and resent DataPacket

            # if processing.processCommand()== ERROR_ACK:
            #     if returned ==ACK then set:





    def __writeToArduino(self, TestCallPath, BName, ser):
        imageParser = ImageParser()
        image = imageParser.parseImage(TestCallPath, BName)
        self.__serialWritePacketStream(image, ser)
        self.__sendDisplayCmd(ser)

        return 0



    """
     | **showBarCode(<BarcodeName>)**:
     |  1. Input : <BarcodeFile.bmp> name
     |  2. Return: Success if DataWritten
     |  3. Please verify with the BarCodeMap.xml
     |  4. sendBarCode() called from BarcodeChanger encapsulation
     """

    def showBarcode(self, BName):
        numOfLines = 0
        try:
            ser = serial.Serial('COM9', 9600, timeout=10, xonxoff=False, rtscts=False, dsrdtr=False)
        except serial.serialutil.SerialException:
             print ('exception - Can not open device COM9')
             return -1

        if ser.isOpen():
            try:
                # ser.flushInput()  # flush input buffer, discarding all its contents
                # ser.flushOutput()  # flush output buffer, aborting current output


                if self.__writeToArduino(self.__path, BName, ser) == -1:
                    print("Writing to Arduino Failed......")
                    return -1


                # Commented for now- for Testing on XCTU
                # self.__sendDisplayCmd(ser)

                # while True:
                #     response = ser.readline()
                #     print('Serial Response: ',response)
                #


                print("write data: Barcode Written")

            except serial.serialutil.SerialException:
                print ('Exception - Can not Communicate with Arduino')
                return -1

            ser.close()

        else:
            print ("cannot open serial port")
        return 0

    def __processPacket(self, ser, delay, packet=[]):

        time.sleep(delay)
        buf = bytearray(16)
        numOfLines = 0
        ret =0
        commbyte_cnt = 0

        try:
            buffer = ""
            while True:
                ser.write(packet)

                oneByte = ser.readline()

                if oneByte:
                    print('read :', oneByte)
                    # for x in oneByte:
                    #     # print hex(ord(x))
                    #     # print x.decode('utf-8')
                    #     # print(bytes(x))
                    #     print('..')
                else:
                    continue

                byteArray = bytearray(oneByte)
                # print('HEXLIFY Response..',   hexlify(byteArray))
                # splitBytes = byteArray.split(r'\\x')


                numOfLines = numOfLines + 1

                if (numOfLines >= 1):
                    break


                if byteArray[0] == STx:
                    commbyte_cnt = 0
                    print('STX hit....')
                    ret = self.__processCommand(byteArray)


                if byteArray[-1] == ETx:  # method should returns bytes for the ProcessedPacket
                    print('ETX hit....')
                    # waitingForReply = False
                    ret = self.__processCommand(byteArray)

                # else:
                #     buffer += byteArray
                #     commbyte_cnt = commbyte_cnt +1
        except serial.serialutil.SerialException:
            print ('Exception - Can not Communicate with Arduino')

        # print('handler...',ret)
        return ret



    def __checkCRC1(self):
        return 0


    def __processCommand(self, buff ):
        if self.__checkCRC1() == 0:
            if buff[1] == CMD_ACK:
                print("ACK Return..")
                return ERROR_ACK
            if buff[1] == CMD_NAK:
                print("NCK Return..")
                return ERROR_NAK
            if buff[1] == CMD_CFG:
                print("config data Returned...")
                return ERROR_CFGOK
        else:
            return ERROR_NCRC