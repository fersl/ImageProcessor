import io
from math import ceil

def get_bit(x,i):
    assert i in range(8) and 0 <= x < 256
    return (x >> i) & 1

def set_bit(x,i,b):
    assert b in [0,1] and i in range(8) and 0 <= x < 256
    return (x & ~(1 << i)) | (b << i)

class BitArray:
    def __init__(self,length=0):
        self.length = length
        self.buffer = bytearray(ceil(length/8))

    def __getitem__(self, key):
        if isinstance(key,int):
            if key < 0:
                key = key + self.length
            if key >= self.length or key < 0:
                raise IndexError(f'Out of bounds: {key} >= {self.length}')
            else:
                i = key % 8
                n = key // 8
                return get_bit(self.buffer[n],i)
        elif isinstance(key,slice):
            out = 0
            for i in reversed(range(*key.indices(self.length))):
                out = (out << 1) | self[i]
            return out
        else:
            raise TypeError('key must be int or range')

    def __setitem__(self, key, value):
        if isinstance(key,int):
            if key < 0:
                key = key + self.length
            if key >= self.length or key < 0:
                raise IndexError(f'Out of bounds: {key} >= {self.length}')
            else:
                i = key % 8
                n = key // 8
                self.buffer[n] = set_bit(self.buffer[n],i,value)
        else:
            raise TypeError('key must be int')

    def __repr__(self):
        return 'bitarray('+bin(self[:])+')'

    def __len__(self):
        return self.length

    def __add__(self, other):
        result = BitArray()
        for bit in self:
            result.append(bit)
        for bit in other:
            result.append(bit)
        return result

    def append(self, value):
        assert value in [0,1]
        i = self.length % 8
        n = self.length // 8
        if i == 0:
            self.buffer.append(value)
        else:
            self.buffer[n] = set_bit(self.buffer[n],i,value)
        self.length += 1

    def to_file(self,file_or_path):
        if isinstance(file_or_path,io.IOBase):
            file_or_path.write(self.length.to_bytes(4,'little'))
            for b in self.buffer:
                file_or_path.write(b.to_bytes(1,'little'))
        elif isinstance(file_or_path,str):
            with open(file_or_path,'wb') as f:
                self.to_file(f)
        else:
            raise TypeError('argument must be str or file')

    def from_file(file_or_path):
        if isinstance(file_or_path,io.IOBase):
            length = int.from_bytes(file_or_path.read(4),'little')
            bitarray = BitArray(length)
            file_or_path.readinto(bitarray.buffer)
            return bitarray
        elif isinstance(file_or_path,str):
            with open(file_or_path,'rb') as f:
                return BitArray.from_file(f)
        else:
            raise TypeError('argument must be str or file')
