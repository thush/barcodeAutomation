import struct
import array

import sys


class DataPacket:


    # CheckCRC is added for simple BreakDown needs to be Extended
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

    def __chksum(self, data):
        if len(data) % 2 != 0:
            data += b'\0'

        res = sum(array.array("H", data))
        res = (res >> 8) + (res & 0xff)
        res += res >> 8
        return (~res) & 0xff

    def checkCRC(self, pack):
        # Verify checksum by adding the raw data values and taking the lower 8 bits.

        # printing Struct pack
        int_sum = int(pack[4:6], 16)  # PM_A_High
        int_sum += int(pack[6:8], 16)  # PM_A_Low
        int_sum += int(pack[8:10], 16)  # PM_B_High
        int_sum += int(pack[10:12], 16)  # PM_B_Low
        int_sum += int(pack[12:14], 16)  # PM_C_High
        int_sum += int(pack[14:16], 16)  # PM_C_Low

        int_sum = int_sum & 0xff
        checksum = int(pack[18:20], 16)

        if (int_sum != checksum):
            return False
        # print int_sum , checksum
        return True



    """
      | **createPacket**:
      |  1. Input: cmd, Payload[]
      |  2. Print: Packet structure in python
      |  3. Please verify with the Packet struct defined on Design
      """
    def createDataPacket(self, payload=[]):
        packetSize = len(payload)
        #packetSize = 1+ len(payload) is discarded as 'Data Pkt size' exceeds 128

        # crc = self.CheckCRC(struct.pack('{}B'.format(len(payload)), *payload ))
        # crc = self.__chksum(struct.pack('{}B'.format(len(payload)),  *payload))
        # return struct.pack('{}B'.format(packetSize), *(payload + crc))
        return struct.pack('{}B'.format(packetSize), *(payload))



    """
     | **DisplayPacket**:
     |  1. Input: packet
     """
    # def DisplayPacket(self, packet):
    #     print('DataPacket:' , hexlify(packet))
