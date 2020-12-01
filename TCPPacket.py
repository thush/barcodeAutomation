import struct
import array

class TCPPacket:
    def __init__(self,
                 src_host,
                 src_port,
                 dst_host,
                 dst_port,
                 flags=0):
        self.src_host = src_host
        self.src_port = src_port
        self.dst_host = dst_host
        self.dst_port = dst_port
        self.flags = flags

    def build(self):
        packet = struct.pack(
            '!HIIBBH',
            self.src_port,  # Source Port
            self.dst_port,  # Destination Port
            0,  # Sequence Number
            0,  # Acknoledgement Number
            5 << 4,
            self.flags,
            8192,
            0,  # Checksum (initial value)
            0 )

    def chksum(packet):
        if len(packet) % 2 != 0:
            packet += b'\0'

            res = sum(array.array("H", packet))
            res = (res >> 16) + (res & 0xffff)
            res += res >> 16

            return (~res) & 0xffff