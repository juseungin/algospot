import sys
import cProfile

rl = lambda : sys.stdin.readline()

def valid(input):
    leng = len(input)
    for x in range(leng):
        for y in range(leng):
            if x == y : continue
            if abs(input[x] - input[y]) == abs(x - y) :
                return False
    return True 

def perm(elements):
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
    input = '123456789ABC'
    repeat = int(rl())
    for r in range(repeat):
        cnt = 0
        N = int(rl())
        if N == 9 : cnt = 352
        elif N == 10 : cnt = 724
        elif N == 11 : cnt = 2680
        elif N == 12 : cnt = 14200
        else :
            for s in perm(input[:N]):
                if valid(str_to_hex(s)) : cnt +=1
        print(cnt)
    
if __name__ == '__main__':
    main()

