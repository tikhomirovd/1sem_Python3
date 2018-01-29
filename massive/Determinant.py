def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    

def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))

n = int(input('Введите порядок матрицы '))
a = [[float(j) for j in input().split()] for i in range(n)]
print(determinant(a))