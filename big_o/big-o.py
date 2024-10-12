# Big O(1)
# Independente do tamanho do input, só será percorrido uma vez
def first_example(nums):
  print(nums[0]) 

# Big O(n) n = quantidade de items
# A complexidade se limita pelo tamanho do meu input
def second_example(nums):
  for i in nums:
    print(i) # Big O(1)

second_example([1,2,3])