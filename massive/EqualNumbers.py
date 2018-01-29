# Данная программа находить максимальное кол-во одинаковых чисел
# В случайном массиве
# Тихомиров Дмитрий
# x - размерность массива
# A - исходный массив
# i,j - счетчики
# D - массив с элементами
# maximum - ответ

from random import randint
x = input('Введите размерность массива ')
if x.isdigit():
    x = int(x)
    D = [0] * x
    A = [int(randint(-10, 10)) for i in range(x)]
    print(A)
    print()
    for i in range(len(A)):
        for j in range(1, len(A)):
            if A[i] == A[j]:
                D[i] += 1
    maximum = max(D)
    print('Количество одинаковых чисел =', maximum)
else:
    print('Введите число')