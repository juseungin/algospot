import sys
# for ol in permutations('ABC'):
#     print(ol)

rl = lambda : sys.stdin.readline()

def valid(input):
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j : continue
            if input[i] - input[j] == i - j :
                return False
    return True 


def perm (elements):
    if len(elements) == 1:
        yield elements
    else:
        for p in perm(elements[1:]):
            for i in range(len(elements)):
                yield p[:i] elements[0],p[i:]


N = '123456789ABC'

input = '123'

for ol in perm([1,2,3]):
    print(ol)
