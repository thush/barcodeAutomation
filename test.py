from itertools import islice

import numpy as np
import serial
from serial.serialutil import *

from CommandPacket import CommandPacket
from DataPacket import DataPacket
from processPacket import processPacket

"""
 | **COMMANDS IN HEX FORM**:
 |
"""
STX = 0x02
ETX = 0x03
ACK = 0x06
NAK = 0x25
VAL = 0x07

EINK_SET_CONFIG = 0x22
EINK_BLKN_CHUNK = 0x23
EINK_DISPLAY = 0x24
EINK_CLEAR = 0x25
EINK_GET_CONFIG = 0x26

ZOOM_LEVEL = 0x01
CHUNK_SIZE = 0x32
TIME_OUT = 0x05

CMD_ACK = 0x6
CMD_NAK = 0x25
STx = 0x2
ETx = 0x3


ser = 0


def splitToChunks(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def serialWritePacketStream(packetStr):
    lst = list(splitToChunks(packetStr, 128))
    time.sleep(0.5)

    print("Size of....: ", len(lst))

    for i in range(0, len(lst)):
        # arr = np.array(lst[i])
        arr = np.array(lst[i])

        dataPacket = DataPacket()
        packedData = dataPacket.createDataPacket(arr)
        return packedData


"""
 | **packData(<DataPacket>)**:
 |  1. [dataChunk] Calling DataPacket Object with dataChunk 
 |  2. Return: Packet packed
 |  3. Please verify with the Packet struct defined on DataPacket.py
 """
def sendData(dataloda=[]):

    dataPacketObject = DataPacket()


    packet = dataPacketObject.createDataPacket(dataload)
    return  packet


"""
 | **createPacket(<CommandPacket>)**:
 |  1. Input <CommandPacket Parameters> 
 |  2. Please verify with the Packet struct defined on CommandPacket.py
 """



def commandsSend():
    cmdPacketObj = CommandPacket()
    # packet= cmdPacketObj.createPacket(EINK_CLEAR)
    # cmdPacketObj.DisplayPacket(packet)


    processedObj = processPacket()

    # BLNK_CHUNK CMD Send ChunkWise
    packet = cmdPacketObj.createPacket(EINK_BLKN_CHUNK)
    cmdPacketObj.DisplayPacket(packet)

    if processedObj.processCommand()  == CMD_ACK:
        # sendData()
    # Datapacket Called with 128 Chunk
        serialWritePacketStream()

    else:
        return -1


    # testload = [ZOOM_LEVEL, CHUNK_SIZE, TIME_OUT]
    testload =[ 0x00, CHUNK_SIZE, TIME_OUT]
    packet = cmdPacketObj.createPacket(EINK_SET_CONFIG, testload)
    cmdPacketObj.DisplayPacket(packet)
    # # expected CommandPacket [STX,0x22,0x08,0x01,0x20,0x05,CRC,ETX]


    # packet = cmdPacketObj.createPacket(EINK_DISPLAY)
    # cmdPacketObj.DisplayPacket(packet)
     # expected CommandPacket [STX,0x24,0x05,CRC,ETX]


    # TODO:Pack all the Packets respectively on a List to Serial.write()..


    try:
        ser = serial.Serial('COM9', 9600, timeout=10, xonxoff=False, rtscts=False, dsrdtr=False)

    except serial.serialutil.SerialException:
        print ('exception - Can not open device  COM')
    if ser is None:
        raise SerialException("Port must be configured before it can be used.")

    numOfLines = 0

    if ser.isOpen():
        try:
            ser.flushInput()  # flush input buffer, discarding all its contents
            ser.flushOutput()  # flush output buffer, aborting current output


            while True:
                ser.write(packet)


                response =ser.readline()
                # response =ser.readlines(1)
                # response = ser.read_until('\x06')
                # print('UART', response)

                numOfLines = numOfLines + 1

                if (numOfLines >= 2):
                    break


            while True:
                response = ser.readline()
                print(response)


        except serial.serialutil.SerialException:
            print ('Exception - Can not Communicate with Arduino')


        ser.close()

    else:
        print ("cannot open serial port")


commandsSend()