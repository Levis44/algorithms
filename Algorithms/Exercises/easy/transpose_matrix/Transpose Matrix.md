[[Transpose Matrix.excalidraw]]

You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

```python
# Input 1
matrix = [
  [1, 2],
]

# Output 1
[
  [1],
  [2]
]

-----------------

# Input 2
matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
]

# Output 2
[
  [1, 3, 5],
  [2, 4, 6]
]

```
## Solução
- List with all necessary positions, so that you just use index instead of another array (memory)
[[List Comprehension]]:
```python
x = [[0 for _ in range(matrix_rows)] for _ in range(matrix_columns)]
```
- Iterate on rows and columns to swap items
```python
transposedMatrix[column][row] = matrix[row][column]
```

Time complexity -> O(h * w)