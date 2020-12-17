from .util import BytesReader


class BitmapHeader():
    def __init__(self, data: bytes):
        self.file_header = BitmapFileHeader(data)
        self.info_header = BitmapInfoHeader(data)


class BitmapFileHeader(BytesReader):
    def __init__(self, data: bytes):
        super().__init__(data)
        self.type = self.readWord(0x0000)
        self.file_size = self.readDWord(0x0002)
        self.reserved_1 = self.readWord(0x0006)
        self.reserved_2 = self.readWord(0x0008)
        self.offset_bits = self.readWord(0x000a)


class BitmapInfoHeader(BytesReader):
    def __init__(self, data: bytes):
        super().__init__(data)
        self.size = self.readDWord(0x000e)
        self.width = self.readLong(0x0012)
        self.height = self.readLong(0x0016)
        self.planes = self.readWord(0x001a)
        self.bit_count = self.readWord(0x001c)
        self.compression = self.readDWord(0x001e)
        self.size_image = self.readDWord(0x0022)
        self.x_pels_per_meter = self.readLong(0x0026)
        self.y_pels_per_meter = self.readLong(0x002a)
        self.clr_used = self.readDWord(0x002e)
        self.clr_important = self.readDWord(0x0032)
