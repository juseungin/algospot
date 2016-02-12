import sys

rl = lambda : sys.stdin.readline()

clocks = [12,9,9,12,12,12,12,12,12,12,12,12,12,12,12,12]
buttons = ((1,2),(3,4))
# ((0, 1, 2), (3, 7, 9, 11) , (4, 10, 14, 15), (1, 2, 3, 4, 5))

def is_all_12(clocks):
    for clock in clocks:
        if clock != 12:
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
        temp[index] += int(n) * 3
        if temp[index] > 12: temp[index] =  temp[index] % 12
 
def push_buttons(buttons):
    for buttons_combi in make_combination(buttons):
        temp = clocks[:] 
#         print(buttons_combi)
        for i in range(len(buttons_combi)):
            if buttons_combi[i] != '0' :
                push(temp, buttons[i], buttons_combi[i])
        if is_all_12(temp) :
            cnt = 0
            for c in buttons_combi:
                cnt += int(c)
            print(cnt, 'times move')
        
def main():
    global buttons
    push_buttons(buttons)
    
main()

