N = int(input('Введите размерность массива '))
A = list(map(float, input('Введите первый массив ').split()))
B = list(map(float, input('Введите второй массив ').split()))
sum = 0
for i in range(N):
    sum += A[i] * B[i]
print('Скалярное произведение равно ', sum)