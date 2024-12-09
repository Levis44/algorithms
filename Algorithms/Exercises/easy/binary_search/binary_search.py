import math

def binarySearch(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1

    if right_pointer < 0:
        return -1

    if right_pointer == 0:
        if target == array[right_pointer]:
            return right_pointer
        else:
            return -1
        
    
    while left_pointer <= right_pointer:
        mid_pointer = math.ceil((left_pointer + right_pointer) / 2)
        
        tentative = array[mid_pointer]

        if target == tentative:
            return mid_pointer

        if target < tentative:
            right_pointer = mid_pointer - 1

        if target > tentative:
            left_pointer = mid_pointer + 1

    return -1
