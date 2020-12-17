def int_to_bytes(value: int, byte_length: int = 4):
    return value.to_bytes(byte_length, byteorder='little', signed=True)


def uint_to_bytes(value: int, byte_length: int = 4):
    return value.to_bytes(byte_length, byteorder='little')


def bytes_to_int(value: bytes):
    return int.from_bytes(value, byteorder='little', signed=True)


def bytes_to_uint(value: bytes):
    return int.from_bytes(value, byteorder='little')


class BytesReader():
    def __init__(self, data: bytes):
        self.data = data

    def readWord(self, offset: int):
        return bytes_to_uint(self.data[offset:offset + 2])

    def readDWord(self, offset: int):
        return bytes_to_uint(self.data[offset:offset + 4])

    def readLong(self, offset: int):
        return bytes_to_int(self.data[offset:offset + 4])
