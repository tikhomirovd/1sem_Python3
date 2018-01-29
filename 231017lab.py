from random import*
import random
n = int(input('Введите размерность матрицы '))
x = [[float(j) for j in input().split()] for i in range(n)]
pr = 1
z = -1
while z < n - 1:
    z += 1
    a = x[z][z]
    if a != 0:
        pr = pr*a
        for i in range(n):    
            x[z][i] = x[z][i]/a

    for i in range(z+1,n):
        b = x[i][z]
        for j in range(n):
            x[i][j] = x[i][j] - x[z][j]*b

d = x[n-1][n-1] * pr
print(d)
