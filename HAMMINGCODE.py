import sys

rl = lambda : sys.stdin.readline()
n = int(rl())

def syndrome(check):
    dec = 0
    for i in range(len(check)):
        dec += pow(2,i) * check[i]
    return dec
    
def corrected_list(encoded_message):
    m = []
    for c in encoded_message:
        m.append(int(c))
#     print(m)
    
    s_check = []
    s_check.append(m[0]^m[2]^m[4]^m[6])
    s_check.append(m[1]^m[2]^m[5]^m[6])
    s_check.append(m[3]^m[4]^m[5]^m[6])
    
    i_syndrome = syndrome(s_check)
    
    if i_syndrome ==0 : return m
    if m[i_syndrome-1] == 1: m[i_syndrome-1] =0
    else : m[i_syndrome-1] = 1
    return m

def decode_message(str_m):
    l_correct = corrected_list(str_m)
    s_decoded_message = str(l_correct[2]) + str(l_correct[4]) + str(l_correct[5]) + str(l_correct[6])
    print(s_decoded_message)

if __name__ == '__main__':
    data = []
    for count in range(n):
        str_m = rl().strip('\n')
        data.append(str_m)
    for str_m in data:
        decode_message(str_m)
