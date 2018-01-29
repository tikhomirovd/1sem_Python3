N = int(input('Введите размерность массива '))
x = list(map(float, input('Введите массив ').split()))
maxN = minN = 0
maximum = minimum = x[0]
sum = 0
for i in range(len(x)):
    if x[i] > maximum:
        maximum = x[i]
        maxN = i
    if x[i] < minimum:
        minimum = x[i]
        minN = i
for i in range(minN, maxN + 1):
    sum += x[i]

a = sum / abs(maxN + 1 - minN)
print('Максимальное значение равно', maximum,
      'и достигается на', maxN + 1, 'элементе')
print('Минимальное значение равно', minimum,
      'и достигается на', minN + 1, 'элементе')
print('Среднее значение от минимума до максимума равно ', a)

