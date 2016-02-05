import sys

rl = lambda : sys.stdin.readline()
n = int(rl())
data = []

def convert(hex_str):
    convert_str = ""
    convert_str +=hex_str[6:8]
    convert_str +=hex_str[4:6]
    convert_str +=hex_str[2:4]
    convert_str +=hex_str[0:2]
    return convert_str

for count in range(n):
    num = int(rl())
    data.append(num)

for num in data:
    s = str(format(num,'08x'))        
    convert_str = convert(s)
    hex_str = '0x' + convert_str
    print(int(hex_str,16))
