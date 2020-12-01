import thread

import serial
import array
from serial.serialutil import *
from CommandPacket import CommandPacket
from binascii import hexlify


CMD_ACK = 0x06
CMD_NAK = 0x25
STx = 0x02
ETx = 0x03

CMD_CFG = 0x29

ERROR_ACK = 0
ERROR_NAK = 1
ERROR_CFGOK = 2
ERROR_CFGNOK = 3
ERROR_NCRC = 4

EINK_SET_CONFIG = 0x22
EINK_BLKN_CHUNK = 0x23
EINK_DISPLAY = 0x24
EINK_CLEAR = 0x25
EINK_GET_CONFIG = 0x26

ZOOM_LEVEL = 0x01
CHUNK_SIZE = 0x32
TIME_OUT = 0x05
ser = 0

try:
    ser = serial.Serial('COM9', 9600, timeout=10, xonxoff=False, rtscts=False, dsrdtr=False)
except serial.serialutil.SerialException:
    print ('exception - Can not open device  COM')
if ser is None:
    raise SerialException("Port must be configured before it can be used.")
waitingForReply = True



cmdPacketObj = CommandPacket()
packet = cmdPacketObj.createPacket(EINK_DISPLAY, 0)
cmdPacketObj.DisplayPacket(packet)
# ...Test-packet created as above...
#

def processPacket(delay, packet=[]):
    time.sleep(delay)
    commbyte_cnt = 0
    hasStarted = False
    buf = bytearray(16)
    numOfLines = 0

    if ser.isOpen():
        try:
            buffer = ""
            while True:
                ser.write(packet)

                oneByte = ser.readline()

                if oneByte:
                    for x in oneByte:
                        # print hex(ord(x))
                        # print x.decode('utf-8')
                        print bytes(x)
                else:
                    continue

                byteArray = bytearray(oneByte)
                print('HEXLIFY Response..',   hexlify(byteArray))
                # splitBytes = byteArray.split(r'\\x')

                # print(type(oneByte))
                print('Response sent..', oneByte)

                numOfLines = numOfLines + 1

                if (numOfLines >= 2):
                    break


                if byteArray[0] == STx:
                    commbyte_cnt = 0
                    # print('STX hit....')
                    ret = processCommand(byteArray, 0)


                if byteArray[-1] == ETx:  # method should returns bytes for the ProcessedPacket
                    print('ETX hit....')
                    waitingForReply = False
                    ret = processCommand(byteArray, 0)
                    return ret

                else:
                    buffer += byteArray
                    commbyte_cnt = commbyte_cnt +1
        except serial.serialutil.SerialException:
            print ('Exception - Can not Communicate with Arduino')

    ser.close()

    return ret


def checkCRC1():
    return 0


def processCommand(buff, count):
    if checkCRC1()== 0:
        if buff[1] == CMD_ACK:
            print("ACK Return..")
            return ERROR_ACK
        if buff[1] == CMD_NAK:
            print("NCK Return..")
            return ERROR_NAK
        if buff[1] ==CMD_CFG:
            print("config data Returned...")
            return ERROR_CFGOK
    else:
        return ERROR_NCRC

    """
     | **processPacket(<processPacket for ACK/NAK/Configs>)**:
     |  1. Input : CommandPacket packed
     |  2. Return: 
     |  3. Please verify with CommandPacket for Command packet packing
     """
# processPacket()


processPacket(1.5, packet)

# Created threads as below
# try:
#    thread.start_new_thread(processPacket, (2, packet,))
# except:
#    print "Error: unable to start thread"
#
# while 1:
#    pass
