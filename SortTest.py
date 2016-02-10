from random import randrange
import time

def insertion(arr):
    for start_index in range(1,len(arr)-1):
        temp = arr[start_index]
        insert_index = start_index
        
        while insert_index != 0  and arr[insert_index -1] > temp:
            arr[insert_index] = arr[insert_index -1]
            insert_index -= 1
        arr[insert_index] = temp
    return arr

def selection(arr):
    leng = len(arr)
    for start_index in range(0, leng -1):
        min_index = start_index
        first_index = start_index
        while start_index < leng -1:
            if arr[start_index] > arr[start_index +1]:
                min_index = start_index + 1
            start_index += 1
        arr[min_index],arr[first_index] = arr[first_index], arr[min_index]
    return arr

def heapify(arr):
    leng = len(arr)
    for i in range(leng -1, 0, -1):
        if i % 2 == 0:
            p = (i - 2) // 2
        else:
            p = (i - 1) // 2
        
        if arr[i] > arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
    return arr

def heap_sort(arr):
    leng = len(arr)
    arr = heapify(arr)
    
    for i in range(1,leng):
        arr[leng-i], arr[0] = arr[0], arr[leng-i]
        arr[:leng-i] = heapify(arr[:leng-i])  

    return arr

def merge(left, right):
    result = []
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else :
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]    
    return result

def merge_sort(arr):
    leng = len(arr)
    if leng <= 1:
        return arr
    
    mid = leng // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def main():
#     list = [7,5,10,4,3,9,1,2,6,8]
    list = []
    for i in range(1000):
        list.append(randrange(1001))
#     print(insertion(list))
#     print(selection(list))
#     print(heap_sort(list))
    print(list)
    start = time.time()
    merge_sort(list)
#     heap_sort(list)
    print(time.time() - start, ' ms')            
main()
