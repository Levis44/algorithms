# O(w*h)
def transposeMatrix(matrix):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])

    transposedMatrix = [[0 for _ in range(matrix_rows)] for _ in range(matrix_columns)]
    for column in range(matrix_columns):
        for row in range(matrix_rows):
            transposedMatrix[column][row]  =  matrix[row][column]
            
    return transposedMatrix

matrix = [
  [1, 4],
  [2, 5],
  [3, 6]
]

print(transposeMatrix(matrix))