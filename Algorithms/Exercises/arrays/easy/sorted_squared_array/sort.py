# time O (n log n) -> para dar um sort
# space O(n)
def sort(array):
    squared_array = []
    for num in array:
        squared_array.append(num ** 2)
    
    squared_array.sort()
    return squared_array

# time O (nˆ2) -> insert
# space O(n)
def pointer(array):
    left_pointer = 0
    right_pointer = len(array) - 1
    
    sorted_squared_array = []
    while left_pointer <= right_pointer:
        num_left = abs(array[left_pointer])
        num_right = abs(array[right_pointer])
        
        if left_pointer == right_pointer:
            sorted_squared_array.insert(0, num_left ** 2) 
            break
        if num_left > num_right:
            sorted_squared_array.insert(0, num_left ** 2)
            left_pointer += 1
        if num_left < num_right:
            sorted_squared_array.insert(0, num_right ** 2)
            right_pointer -= 1
        if num_left == num_right:
            sorted_squared_array.insert(0, num_right ** 2)
            sorted_squared_array.insert(0, num_left ** 2)
            right_pointer -= 1
            left_pointer += 1

    return sorted_squared_array

# O(n) -> time and space
def refactor_pointer(array):
    length = len(array)
    left_pointer = 0
    right_pointer = length - 1
    
    sorted_squared_array = [0] * length
    idx = length - 1
    
    while left_pointer <= right_pointer:
        num_left = abs(array[left_pointer])
        num_right = abs(array[right_pointer])
        
        if num_left > num_right:
            sorted_squared_array[idx] = num_left ** 2
            left_pointer += 1
        else: 
            sorted_squared_array[idx] = num_right ** 2
            right_pointer -= 1
        idx -= 1
        

    return sorted_squared_array
    