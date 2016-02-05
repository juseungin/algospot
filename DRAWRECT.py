import sys

rl = lambda : sys.stdin.readline()
n = int(rl())

data_xy = []
# 문자열 입력받는 부분
for count in range(n):
    for i in range(3):
        str = rl()
        data_xy.append(str.strip('\n').split(' '))

# print(data)
# x 좌표를 얻어오는 함수 
def find_x(data):
    x = []
    key_x = {}
    for j in range(3):
        x.append(int(data[j][0]))
    # 키를 만들기
    for k in range(3):
        key_x[x[k]]=0
    for v_x in x:
        key_x[v_x] +=1
    for k_x in key_x:
        if key_x[k_x] == 1:
            return k_x

def find_y(data):
    y = []
    key_y = {}
    for j in range(3):
        y.append(int(data[j][1]))
    # 키를 만들기
    for k in range(3):
        key_y[y[k]]=0
    for v_y in y:
        key_y[v_y] +=1
    for k_y in key_y:
        if key_y[k_y] == 1:
            return k_y

# m*3:m*3+3
for m in range(n):
    print(find_x(data_xy[m*3:m*3+3]),find_y(data_xy[m*3:m*3+3]))
