N = int(input('Введите количество чисел в массиве '))
t = float(input('Введите значение переменной t '))
A = [0] * N
a = 0
b = 0
c = 0
amin = 0
aminj = 0

for j in range(N):
    A[j] = (j - t) * (j - t) / 2 - 3
    print(A[j], end = ' ')
print()
if N == 1:
    print('Последовательность общего типа')
else:
    for j in range(N - 1):
        if A[j + 1] > A[j]:
            a += 1
        elif A[j + 1] < A[j]:
            b += 1
    if a == N - 1:
        print('Последовательность является возрастающей')
    elif b == N - 1:
        print('Последовательность является убывающей')
    else:
        print('Последовательность общего типа')

maximum = A[0]
jmax = 0


for j in range(N):
    if A[j] > maximum:
        maximum = A[j]
        jmax = j
for j in range(N):
    if A[j] < 0:
        c += 1
        aminj = j
        break

if c == 0:
    print('Отрицательных элементов нет ')
else:
    A[aminj], A[jmax] = A[jmax], A[aminj]
for j in range(N):
    print(A[j], end = ' ')
