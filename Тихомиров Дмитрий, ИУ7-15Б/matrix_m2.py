# Тихомиров ИУ7-15Б
# Матрица м-2

print(ord('0'))
try:
    print('Введите размерность матрицы ')
    n = int(input())
    m = int(input())
except ValueError:
    print('Нужны целые числа ')
else:
    if 1 <= n <= 6 and 1 <= m <= 8:
        A = []
        d = [0] * m
        print('Вводите через пробел')
        for i in range(n):
            row = list(input().split())
            A.append(row)
        if len(A[i]) <= 8:
            for i in range(n):
                for j in range(len(A[i])):
                    if 48 <= ord(A[i][j]) <= 57:
                        A[i][j] = '#'
                        d[j] += 1
            for i in range(n):
                if '#' in A[i]:
                    for j in range(len(A[i])):
                        A[i][j] = '#'
            for k in range(n):
                z = d[k]
                if z != 0:
                    for i in range(n):
                        for j in range(len(A[i])):
                                A[i][k] = '#'
    else:
        print('Проверь условие и введи верные данные ')

    for i in range(n):
        print(A[i])
