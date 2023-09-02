import random
def binary_search(lst, search): # binary search happens on sorted array only
    print(lst)
    lst = sorted(lst)
    low, high = 0, len(lst) -1

    while low <= high:
        mid = low+ (high-low)//2

        if lst[mid] == search:
            return mid
        
        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4
random.shuffle(array)
print(binary_search(array, x))