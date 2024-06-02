import struct
from Cython.Build.BuildExecutable import build

def check_32_bit_system():
    bit_size = struct.calcsize("P") * 8
    return bit_size == 32

def check_64_bit_system():
    bit_size = struct.calcsize("P") * 8
    return bit_size == 64

if check_32_bit_system():
    #print("This is a 32-bit system.")
    build("hchk.py")
elif check_64_bit_system():
    #print("This is a 64-bit system.")
    build("hchk.py")
else:
    print("Unable to determine system architecture.")
