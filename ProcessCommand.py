import serial
from serial.serialutil import *


ACK = 0x06
NAK = 0x25
STx = 0x02
ETx = 0x03
ConfigCmd = 0x26
CONFIG = 0x29


ser = 0
try:
    ser = serial.Serial('COM9', 9600, timeout=10, xonxoff=False, rtscts=False, dsrdtr=False)

except serial.serialutil.SerialException:
    print ('exception - Can not open device  COM')
if ser is None:
    raise SerialException("Port must be configured before it can be used.")

numOfLines = 0
buf = bytearray(8)



def processPacket():

    MAX_PACKET_SIZE =128
    comm_buff = [MAX_PACKET_SIZE]
    commbyte_cnt = 0
    hasStarted = False


    if ser.isOpen():
        x = ser.readline()
        # x = ser.read_until()
        print('response.. ', x)

        while True:
            if (x[0] == STx):
                print("STX Received: " , (str(x[0])))
                commbyte_cnt = 0
                return

            if (x[4] == ETx):
                print("ETX Received: " , (to_bytes(x[4])))
                # processCommand(comm_buff ,commbyte_cnt)
                commbyte_cnt = 0
                return

            if(commbyte_cnt < (MAX_PACKET_SIZE - 1) ):
                print("CMD Received :" ,x )
                comm_buff[commbyte_cnt ] = x
                commbyte_cnt =commbyte_cnt +1



# def processCommand():
    # if (x == ACK):
    #     print("ACK Received: ", (to_bytes(x)))
    #     commbyte_cnt = 1
    #     return
    #
    # if (x == NAK):
    #     print("NACK Received: " + (to_bytes(x)))
    #     processCommand(comm_buff ,commbyte_cnt)
    #     commbyte_cnt = 1
    #     return

    # if (x == CONFIG):
    #     print("CONFIGURATION Received: " + (to_bytes(x)))
    #     # processCommand(comm_buff ,commbyte_cnt)
    #     commbyte_cnt = 1
    #     return