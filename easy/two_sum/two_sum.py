from typing import List

class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] +  nums[j] == target:
                        return [i, j]
        return []
    
    def twoSortingTwoPointers(self, nums: List[int], target: int) -> List[int]:
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
    def hashRefactor(self, nums: List[int], target: int) -> List[int]:
        hasher = {}

        for idx, value in enumerate(nums):
            if hasher.get(value) is not None:
                return [hasher.get(value), idx]
            hasher[target-value] = idx
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15, 1]
    target = 9

    solution = Solution()

    result = solution.hash(nums, target)
    print(f"Indices: {result}")