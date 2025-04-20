import struct


class RSMetaType:
    CLIENT_PUT = 1
    CLIENT_GET = 2

    SERVER_OK = 3
    SERVER_SEND = 4


class RSMsgDelimiter:
    RSJOINBLOCK = "<RSJOINBLOCK>"


class RSMetaMsg:
    def __init__(self, meta_type: RSMetaType, meta_len: int=0):
        self.meta_type = meta_type
        self.meta_len = meta_len

    def serialize(self) -> bytes:
        packed_data = struct.pack("ii", self.meta_type, self.meta_len)
        return packed_data

    @staticmethod
    def deserialize(bdata: bytes) -> "RSMetaMsg":
        mtype, mlen = struct.unpack("ii", bdata)
        return RSMetaMsg(mtype, mlen)

    @staticmethod
    def get_size() -> int:
        return struct.calcsize("ii")
