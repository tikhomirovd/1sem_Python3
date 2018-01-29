n = int(input('Введите количество чисел в массиве '))

print('Введите число ')
print('Вводим массив')
    # Вводим элементы массива A
i = 0

A = []
    # Проверка на то, что вводят число
for j in range(n):
    x = input()
    if x.isdigit():
        A.append(int(x))
if len(A) == 0:
    print('Введите хотя бы одно число ')
else:
    D = [0]*len(A)
    for q in range(1, len(A)):
        if A[q] > A[q - 1]:
            D[i] += 1
        else:
            i += 1
    maximum = max(D)
    z = D.index(max(D))
    print(z)
    print(D)

    for i in range(z, z + maximum + 1):
        print(A[i], end = ' ')
    print('Длина наибольшой возрастающей последовательности равна',maximum + 1)

