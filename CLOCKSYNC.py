import sys

rl = lambda : sys.stdin.readline()

clocks = []
buttons = ( (0, 1, 2),
            (3, 7, 9, 11),
            (4, 10, 14, 15),
            (0, 4, 5, 6, 7),
            (6, 7, 8, 10, 12),
            (0, 2, 14, 15),
            (3, 14, 15),
            (4, 5, 7, 14, 15),
            (1, 2, 3, 4, 5),
            (3, 4, 5, 9, 13) )

def is_all_12(clocks):
    for clock in clocks:
        if clock != 4:
             return False
    return True

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def make_combination(buttons):
    for n in range(pow(4,len(buttons))):
        i_buttons = convert(n, 4)
        zero_count = len(buttons) - len(i_buttons)
        f_button = '0' * zero_count + i_buttons
        yield f_button
    
def push(temp, indexes, n):
    for index in indexes:
        temp[index] += int(n)
        if temp[index] > 4: temp[index] =  temp[index] % 4
 
def push_buttons(buttons):
    min_move = -1
    for buttons_combi in make_combination(buttons):
        temp = clocks[:]
        for i in range(len(buttons_combi)):
            if buttons_combi[i] != '0' :
                push(temp, buttons[i], buttons_combi[i])
        if is_all_12(temp) :
            cnt = 0
            for c in buttons_combi:
                cnt += int(c)
            if min_move < 0 : min_move = cnt
            elif min_move > cnt : min_move = cnt
            
    print(min_move, 'times move')
        
def main():
    global buttons,clocks
    clocks = rl().split()
    clocks = [int(i)/3 for i in clocks]
    push_buttons(buttons)

if __name__ == '__main__':
    main()
