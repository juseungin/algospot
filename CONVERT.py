import sys

rl = lambda : sys.stdin.readline()
n = int(rl())
data = []
count =1

def kg_to_lb(kg):
    return 2.2046 * kg

def lb_to_kg(lb):
    return 0.4536 * lb

def l_to_g(l):
    return 0.2642 * l

def g_to_l(g):
    return 3.7854 * g


for c in range(n):
    str = rl().strip('\n')
    data.append(str)

    
for str in data:
    token = str.split(' ')
    
    if token[1] == "kg":
        print(count, round(kg_to_lb(float(token[0])),4),'lb')
    elif token[1] == "lb":
        print(count, round(lb_to_kg(float(token[0])),4),'kg')
    elif token[1] == "l":
        print(count, round(l_to_g(float(token[0])),4),'g')
    elif token[1] == "g":
        print(count, round(g_to_l(float(token[0])),4),'l')
    count +=1
