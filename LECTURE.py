import sys

rl = lambda : sys.stdin.readline()
n = int(rl())
data = []

for i in range(n):
    str = rl()
    str.strip('\n')
    data.append(str)

for str in data:
    token = []
    for i in range(int(len(str)/2)):
        token.append(str[i*2:i*2+2])
    token = sorted(token)
    print ("".join(token))
