from typing import List

class Solution:
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] +  nums[j] == target:
                        return [i, j]
        return []
    
    def two_sorting_two_pointers(self, nums: List[int], target: int) -> List[int]:
        # [[valor, indice_original],[valor, indice_original]]
        num_original_index = [(num, i) for i, num in enumerate(nums)]
        num_original_index.sort(key= lambda x: x[0])

        left = 0
        right = len(nums) - 1

        while left < right:
            sum_result = num_original_index[left][0] + num_original_index[right][0]

            if(sum_result == target):
                return [num_original_index[left][1], num_original_index[right][1]]
            elif(sum_result > target):
                right -= 1
            elif(sum_result < target):
                left += 1

        return []
    def hash(self, nums: List[int], target: int) -> List[int]:
       hash = {}
 
       for i in range(len(nums)):
            expected_sum = target - nums[i]
            
            correct_sum_index = hash.get(expected_sum, "-")

            if (correct_sum_index != "-"):
                return [i, correct_sum_index]
            else:
                hash[expected_sum] = i
    def hash_refactor(self, nums: List[int], target: int) -> List[int]:
        hasher = {}

        for idx, value in enumerate(nums):
            if hasher.get(value) is not None:
                return [hasher.get(value), idx]
            hasher[target-value] = idx
    
class Solution_Algo_Expert:
    def solution_1_brute_force(array, targetSum):
        for idx, num in enumerate(array):
            for idx2, num2 in enumerate(array):
                if idx == idx2: 
                    continue
                if num + num2 == targetSum:
                    return [num, num2]
        return []
    
    def solution_1_brute_force_refactor(array, targetSum):
        for idx, num in enumerate(array):
            for idx2, num2 in enumerate(array):
                if idx == idx2: 
                    continue
                if num + num2 == targetSum:
                    return [num, num2]
        return []

    def solution_3_hasher(array, targetSum):
        hasher = {}
        
        for num in array:
            if hasher.get(num) is not None:
                return [num, hasher.get(num)]
            hasher[targetSum - num] = num
        return []
    
    def solution_3_hasher_refactor(array, targetSum):
        hasher = {}
        
        for num in array:
            potencialMatch = targetSum - num
            if potencialMatch in hasher:
                return [potencialMatch, num]
            else: 
                hasher[num] = True
        return []
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15, 1]
    target = 9

    solution = Solution()

    result = solution.hash(nums, target)
    print(f"Indices: {result}")