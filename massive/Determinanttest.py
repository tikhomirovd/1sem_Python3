x = int(input('Введите размерность матрицы '))
m = [[float(j) for j in input().split()] for i in range(x)]
for j in range(x):
    m[0][j] /= m[0][0]
print(m)