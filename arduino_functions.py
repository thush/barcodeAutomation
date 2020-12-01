import struct
from binascii import hexlify

STX = 0x02
ETX = 0x03
ACK = 0x06
NAK = 0x25

CRC8 = 0
EINK_SET_CONFIG = 0x22
EINK_BLKN_CHUNK = 0x23
EINK_DISPLAY = 0x24
EINK_CLEAR = 0x25
EINK_GET_CONFIG = 0x26



def eink_blkn_chunk():
    packet = struct.pack('<BBBBB', STX, EINK_BLKN_CHUNK, 0, CRC8, ETX)
    print(hexlify(packet))
    # send_serial(packet)


def eink_set_setconfig():
    print('blank')


def eink_display():
    packet = struct.pack('<BBBBB', STX, EINK_DISPLAY, 0, CRC8,ETX)


def eink_clear():
    packet = struct.pack('<BBBBB', STX, EINK_CLEAR, 0, CRC8,ETX)
    print(hexlify(packet))
eink_blkn_chunk()


def send_serial(packet):
    status = 0;
    if(packet != ''):
        status= 1

    return status
