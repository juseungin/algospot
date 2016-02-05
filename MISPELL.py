import sys

rl = lambda : sys.stdin.readline()
n = int(rl())
data = []
for count in range(n):
    str = rl().strip('\n')
    data.append(str)
c = 1
for str in data:
    token = str.split(' ')
    new_str = token[1][:int(token[0])-1] + token[1][int(token[0]):]
    print (c,new_str)
    c +=1
