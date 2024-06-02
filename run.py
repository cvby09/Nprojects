import struct,os
from Cython.Build.BuildExecutable import build

def check_32_bit_system():
    bit_size = struct.calcsize("P") * 8
    return bit_size == 32

def check_64_bit_system():
    bit_size = struct.calcsize("P") * 8
    return bit_size == 64

if check_32_bit_system():
    print("This is a 32-bit system.")
elif check_64_bit_system():
    print("This is a 64-bit system.")
else:
    print("Unable to determine system architecture.")
def HEncode(data,output,file):
    # Save the original stdout and stderr
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    try:
        # Redirect stdout and stderr to /dev/null
        sys.stdout = open('/dev/null', 'w')
        sys.stderr = open('/dev/null', 'w')
        # Call the build function
        build(file)
        print("Successful")
    except Exception as e:
        print(f"Build failed: {e}")
    finally:
        # Restore the original stdout and stderr
        sys.stdout = original_stdout
        sys.stderr = original_stderr
os.system("./hchk")
