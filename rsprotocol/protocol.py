import struct


class RSMetaType:
    CLIENT_PUT = 10
    CLIENT_GET = 11
    CLIENT_SAVE = 12

    SERVER_OK = 20
    SERVER_SEND = 21


class RSGetType:
    NOT_RELATED = 30
    WITH_SCORE = 31
    WITHOUT_SCORE = 32

class RSMsgDelimiter:
    RSJOINBLOCK = "<RSJOINBLOCK>"


class RSMetaMsg:
    def __init__(self, meta_type: RSMetaType, get_type: RSGetType, meta_len: int=0):
        self.meta_type = meta_type
        self.get_type = get_type
        self.meta_len = meta_len

    def serialize(self) -> bytes:
        packed_data = struct.pack("iii", self.meta_type, self.get_type, self.meta_len)
        return packed_data

    @staticmethod
    def deserialize(bdata: bytes) -> "RSMetaMsg":
        mtype, gtype, mlen = struct.unpack("iii", bdata)
        return RSMetaMsg(mtype, gtype, mlen)

    @staticmethod
    def get_size() -> int:
        return struct.calcsize("iii")
