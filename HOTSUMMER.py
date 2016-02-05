import sys

rl = lambda : sys.stdin.readline()
n = int(rl())

data = []

for c in range(n*2):
    str = rl().strip('\n')
    data.append(str)

for i in range(n):
    limit = int(data[i*2])
    powers = data[i*2+1].split(' ')
    over = False
    for power in powers:
        limit = limit - int(power)
        if limit < 0:
            over = True
            break
    if over == True:
        print("No")
    else:
        print("Yes")
