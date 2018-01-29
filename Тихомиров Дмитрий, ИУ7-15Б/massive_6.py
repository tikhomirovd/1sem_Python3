# Тихомиров ИУ7-15Б
# Массив 6
i = 0
try:
    i = int(input('Введите размер матрицы '))
except ValueError:
    print('Нужны целые числа ')
else:
    z = 0
    a = [0] * i
    if 1 <= i <= 14:
        print('Введите матрицу построчно ')
        try:
            for i in range(i):
                a[i] = int(input())
        except ValueError:
            print('Пожалуйста, введи построчно')
        else:
                for j in range(i):
                    for k in range(i):
                        if a[k] > a[k + 1]:
                            a[k], a[k + 1] = a[k + 1], a[k]
                x = a[0]
                for j in range(i):
                    if a[j] == a[j + 1] and a[j] != x:
                        print(a[j], end=' ')
                        x = a[j]
                        z += 1
                if z == 0:
                    print('Повторяющихся чисел нет ')
    else:
        print('Массив содержит от 1 до 14 элементов')
