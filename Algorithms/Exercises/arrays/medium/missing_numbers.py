# Time -> O(nˆ2)
# Space -> O(1) 
def missingNumbers1(nums):
    max = len(nums) + 2

    isMissing = []
    for i in range(max):
        if i + 1 not in nums:
            isMissing.append(i + 1)
            
    return isMissing

# Time -> O(n log n)
# Space -> O(n)
def missingNumbers2(nums):
    nums.sort()
    nums_length = len(nums)
    max =  nums_length + 2

    complete_array = [i for i in range(1, max + 1)]
    
    pointer_1 = 0
    pointer_2 = 0

    missing_numbers = []
    while len(missing_numbers) < 2:
        if pointer_1 < nums_length and nums[pointer_1] == complete_array[pointer_2]:
            pointer_1 += 1
            pointer_2 += 1
        else:
            missing_numbers.append(complete_array[pointer_2])
            pointer_2 += 1

    return missing_numbers


# Time -> O(n)
# Space -> O(n)
def missingNumbers3(nums):
    includedNums = set(nums)

    isMissing = []
    for num in range(1, len(nums) + 3):
        if not num in includedNums:
            isMissing.append(num)
            
    return isMissing