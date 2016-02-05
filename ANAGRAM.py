import sys

rl = lambda : sys.stdin.readline()
n = int(rl())
data = []

for count in range(n):
    str = rl().strip('n').split()
    data.append(str);

def compare(data):
    if data[0] == data[1]:
        print('No.')
        return
    if len(data[0]) != len(data[1]):
        print('No.')
        return
    data[0] = sorted(data[0])
    data[1] = sorted(data[1])
    if data[0] == data[1]:
        print('Yes')
    else:
        print('No.')

for count in range(n):
    compare(data[count])
