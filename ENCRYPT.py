import sys

rl = lambda : sys.stdin.readline()
n = int(rl())
data = []

for count in range(n):
    str = rl().strip('\n')
    data.append(str)

for str in data:
    even = []
    odd = []
    for i in range(len(str)):
        if i % 2 == 0 :
            even.append(str[i])
        else :
            odd.append(str[i])
        
    print ("".join(even+odd))
