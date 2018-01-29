n = int(input('Введите кол-во столбцов '))
x = []
print('Введите матрицу ')
for i in range(n):
    x.append([float(j) for j in input().split()])

def print_function(x):
    for n in x:
        for m in n:
            print(m, end=' ')
        print()

def swap_x(index1, index2, iterable):
    for x in iterable:
        x[index1], x[index2] = x[index2], x[index1]

def sort_x(x):
    for k in range(n):
        for i in range(n - 1):
            sum1 = 0
            sum2 = 0
            for j in range(n):
                sum1 += x[j][i]
                sum2 += x[j][i + 1]
            if sum1 > sum2:
                swap_x(i, i+1, x)


def search(x):
    num1 = 0
    num2 = 0
    for i in range(n):
        for j in range(n):
            if i < j and x[i][j] % 5 == 0:
                num1 += 1
            if i > j and x[i][j] % 5 == 0:
                num2 += 1
    if num1 > num2:
        print('В верхнетреугольной больше таких чисел ')
    elif num1 < num2:
        print('В нижнетреугольной больше таких чисел ')
    else:
        print('Количество таких чисел одинаково')

print('Исходный массив ')
print_function(x)
sort_x(x)

print('Отсортированный массив ')
print_function(x)

search(x)



