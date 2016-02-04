import sys

rl = lambda : sys.stdin.readline()

def valid(input):
    for x in range(len(input)):
        for y in range(len(input)):
            if x == y : continue
            if abs(input[x] - input[y]) == abs(x - y) :
                return False
    return True 

def perm (elements):
    if len(elements) == 1:
        yield elements
    else:
        for p in perm(elements[1:]):
            for i in range(len(elements)):
                yield p[:i] + elements[0] + p[i:]

def str_to_hex(string):
    li = []
    for ch in string:
        li.append(int(ch,16))
    return li

def hex_to_str(li):
    out_str= ''
    for num in li:
        if num == 10 : num = 'A'
        elif num == 11 : num = 'B'
        elif num == 12 : num = 'C'
        elif num == 13 : num = 'D'
        elif num == 14 : num = 'E'
        elif num == 15 : num = 'F'
        out_str += str(num)
    return out_str

def main():
    input = [1,2,3,4,5,6,7,8,9,10]
    cnt = 0
    for s in perm(hex_to_str(input)):
        if valid(str_to_hex(s)) : cnt +=1
    print(cnt)
if __name__ == '__main__':
    main()
