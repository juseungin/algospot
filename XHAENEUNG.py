import sys
import re

data = []
rl = lambda: sys.stdin.readline()
n = int(rl())
p = re.compile('[a-z]+')
number_dic = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
number_arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiple(a,b):
    return a*b
def str_to_digit(str):
    return number_dic[str]
def digit_to_str(digit):
    return number_arr[digit]

def compare(str1,str2):
    if len(str1) != len(str2) :
        return "No"
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return "Yes"
    else:
        return "No"

#입력받는 부분
for count in range(n):
    str = rl().strip('\n')
    data.append(str)

# print(data)
for word_list in data:
    word_list = word_list.split(' ')
#     print(word_list)
     
    # operator 
    nums = []
    nums.append(str_to_digit(word_list[0]))
    op = word_list[1]
    nums.append(str_to_digit(word_list[2]))
      
    if op == '+':
        result = plus(nums[0],nums[1])
    elif op == '-':
        result = minus(nums[0],nums[1])
    elif op == '*':
        result = multiple(nums[0],nums[1])
    if result > 10 or result < 0:
        print("No")
    else:
        print(compare(digit_to_str(result),word_list[4]))
