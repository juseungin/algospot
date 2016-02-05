import sys

rl = lambda : sys.stdin.readline()

def match(input):
    l_input = list(input)
    l = len(l_input)
    stack =[]
    
    for i in range(l-1,-1,-1):
        b = l_input[i]
        if b == '(' : 
            if len(stack) == 0 : return 'NO'
            if ')' == stack.pop(): pass 
            else : return 'NO'
        elif b == '{':
            if len(stack) == 0 : return 'NO'
            if '}' == stack.pop(): pass
            else : return 'NO'
        elif b == '[':
            if len(stack) == 0 : return 'NO'
            if ']' == stack.pop(): pass
            else : return 'NO'
        else:
            stack.append(b)
    if len(stack) != 0:
        return 'NO'
    return 'YES'

def main() :
    repeat = int(rl())
    output = []
    for n in range(repeat):   
        input = rl().strip('\n')        
        output.append(match(input))
    for ans in output:
        print(ans)
        
if __name__ == '__main__':
    main()
