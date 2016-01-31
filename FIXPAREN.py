import sys

rl = lambda : sys.stdin.readline()

closer = {'}':'{', ')':'(', '>':'<', ']':'['}
opener = {'{':'}', '(':')', '<':'>', '[':']'}
order = {'{':0, '(':1, '<':2, '[':3 }

def main():
    repeat = int(rl())
    output = []
    for n in range(repeat):
        s, priority = rl().split()
    
        for i in range(4):
            order[priority[i]] = 4-i
        
        stack = []
        ans = []
        seg = []
        pushed = True
        for i in range(len(s)):
            if len(stack) == 0:
                seg = []
            parentheses = s[i]
            if parentheses in closer.keys():
                left = stack.pop()
                if order[left]< order[closer[parentheses]]:
                    left = closer[parentheses]
                    right = parentheses
                else:
                    right = opener[left]
                
                if pushed == True:
                    seg.append(left)
                    seg.append(right)
                else:
                    seg.insert(0, left)
                    seg.append(right)
                pushed = False
                if len(stack) == 0:
                    ans.append(''.join(seg))
                    
            else :
                stack.append(parentheses)
                pushed = True         
        output.append(''.join(ans))
    
    for ans in output:
        print(ans)
    
if __name__ == '__main__':
    main()

# 3
# (} {(<[
# ()([)> <({[
# <{(][>(}>] <[{(
