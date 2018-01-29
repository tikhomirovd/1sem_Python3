n = int(input('Введите количество чисел в массиве '))
A = [0] * n
a = 100000
b = 100000
a1 = 0
b1 = 0
print('Вводим массив ')
for i in range(n):
    A[i] = float(input())
for i in range(n):
    if A[i] < a:
        a = A[i]
        a1 = i
A.remove(A[a1])
for i in range(n - 1):
    if A[i] < b:
        b = A[i]
        b1 = i + 1

print(a, b)
print(abs(a1 - b1) - 1)