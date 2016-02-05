import sys

def make_divisor(n):
    divisors = [1]
    last_index = 0
    for i in range(2,int(n/2)+1):
        if n % i == 0 :
            divisors.append(i)
            last_index +=1
    return divisors, last_index

def sum(d_set):
    s = 0
    for divisor in d_set:
        s += divisor
    return s

def is_subset_sum(d_set, last_index,g):
    if last_index < 0 : return False
    
    last = d_set[last_index]
    last_index -= 1
    if last == g : return True
    if last > g : return is_subset_sum(d_set,last_index, g)
    if last < g :
        if is_subset_sum(d_set, last_index, g - last) == False:
            return is_subset_sum(d_set, last_index-1, g)
        else: 
            return True

def is_weird(a):
    divisors,last_index = make_divisor(a)
    
    if sum(divisors) < a:
        print("not weird")
    else :
        if is_subset_sum(divisors,last_index, a) == False:
            print("weird")
        else:
            print("not weird")


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    count = int(rl())
    data = []
    
    for c in range(count):
        data.append(int(rl()))
        
    for num in data:
        if num % 2 != 0:
            print("not weird")
            continue
        is_weird(num)
