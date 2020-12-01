import sys

import array
import struct
from binascii import hexlify


class CommandPacket:
    STX = 2
    ETX = 3

    def __chksum(self, data):
        if len(data) % 2 != 0:
            data += b'\0'

        res = sum(array.array("H", data))
        res = (res >> 8) + (res & 0xff)
        res += res >> 8
        return (~res) & 0xff


    def CheckCRC(self, Packet):
        try:
            if len(Packet) == 0:
                return False
            ByteArray = bytearray(Packet[:len(Packet) - 2])

            if sys.version_info[0] < 3:
                results = self.ModbusCrc(str(ByteArray))
            else:  # PYTHON3
                results = self.ModbusCrc(ByteArray)

            CRCValue = ((Packet[-1] & 0xFF) << 8) | (Packet[-2] & 0xFF)
            if results != CRCValue:
                self.LogError("Data Error: CRC check failed: %04x  %04x" % (results, CRCValue))
                return False
            return True
        except Exception as e1:
            self.LogErrorLine("Error in CheckCRC: " + str(e1))
            self.LogError("Packet: " + str(Packet))
            return False

    """
      | **createPacket**:
      |  1. Input: cmd, Payload[]
      |  2. Print: Packet structure in python
      |  3. Please verify with the Packet struct defined on Design
      """
    def createPacket(self, cmd, payload):
        packetSize = 5 + 1
        # crc = self.__chksum(struct.pack('{}B'.format(len(payload) + 2), cmd, packetSize, *payload))
        crc = 0x00
        # crc = self.CheckCRC(cmd)
        # print('CRC val:', crc)
        return struct.pack('{}B'.format(packetSize), self.STX, cmd, packetSize, payload, crc, self.ETX)



    # def createPacket(self, cmd, payload):
    #     variableLoad = []
    #
    #     # for x in payload:
    #     #     variableLoad.append(x)
    #     packetSize = 5 + len(variableLoad)
    #     # crc = self.__chksum(struct.pack('{}B'.format(len(payload) + 2), cmd, packetSize, *payload))
    #     crc = 0x00
    #     print('CRC val:', crc)
    #     print(type(variableLoad))
    #     # variableLoad.append(crc)
    #     # variableLoad.append(self.ETX)
    #     return struct.pack('{}B'.format(packetSize), self.STX, cmd, packetSize, (variableLoad), crc, self.ETX)



    """
     | **DisplayPacket**:
     |  1. Input: 
     """
    def DisplayPacket(self, packet):
        print('cmdPkt', hexlify(packet))