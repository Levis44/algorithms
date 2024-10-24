# Return Indices
[O LeetCode que mais cai em entrevista](https://www.youtube.com/watch?v=b7Vy-uIQUrE&ab_channel=AugustoGalego)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```python

# Example 1:
Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

# Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Brute Force

- Tentar todas as combinações possíveis
- Complexidade de O(nˆ2)

Nós podemos pegar 2 ponteiros e iterar sobre os elementos do array para conseguir achar os dois números que somados poderão resultar no target

| -> pointer -> comparar pointers

```
 | |
[2,7,11,15]

 |   |
[2,7,11,15]
```

## Sorting + 2 pointers

- Sort do array O(log n) -> Ordenar
- Complexidade de O(n log n)

Nós podemos começar com dois ponteiros, um no começo da lista e outro no final;
Se a soma dos dois ponteiros for < target -> move o ponteiro da esquerda +1
Se a soma dos dois ponteiros for > target -> move o ponteiro da direita -1

Precisamos salvar os índices da lista original para acessar o valor corretamente.

```
 |      |
[2,7,11,15] -> maior

 |   |
[2,7,11,15] -> maior

 | |
[2,7,11,15] -> achou
```

## Hash

- Hash maps para comparar valores já armazenados
- Complexidade de O(n)

Utilizar um hash map com os valores dos index:

```
 |
[2,15,7,11]

Qual o número somado com 2 da o target? 7
{7: 0}

   |
[2,15,7,11]

Qual o número somado com 15 da o target? -6
{7: 0, -6: 1}

      |
[2,15,7,11]

7 Está no hashmap? Se sim retorna os indexes
{7: 0, -6: 1}
```

# Return Nums
  
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

```python
# Inpunt
array = [3,4,5]
targetSum = 8

# Output
[3,5]
```

## Brute force
2 for loops until targetSum
O(nˆ2) time | O(1) space

## Sort + 2 pointers
sort + pointer left and right
O(n log(n)) | O(1) space

## Hash
Hash map e 1 for loop
O(n) time | O(n) space