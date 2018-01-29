''' Назначение программы: вычислить таблицу значений функций
на промежутке, построить график одной из функций.

Фамилия: Тихомиров

Описание переменных:
r - аргумент функций (сначала начальное значение),
k - конечное значение,
sh - шаг,
n - кол-во вычисляемых значений (кол-во строк таблицы),
x,y - массивы значений функции по оси х и y соответственно,
f1,f2 - значение функций от аргумента r(временное хранение - позже в массивах),
l - длина оси Y на графике (в символах),
maxy,miny - наибольшее и наименьшее значение, принимаемые функцией
на заданном диапозоне, график которой строится,
m,mo - расстояние на котором должны ставиться * и | в каждой строке графика
maxf2, minf2 - максимальное и минимально значение функции f2'''

from math import log, exp

z = float(input('Введите начальное значение '))
k = float(input('Введите конечное значение '))
sh = float(input('Введите шаг '))
count = 0
n = int((abs(k - z)) / abs(sh) + 1)
y = n * [0]
x = n * [0]
z = z - sh
maxf2 = -100000
minf2 = 100000

print('\u250C', 6 * '\u2500', '\u252C', 11 * '\u2500', '\u252C', 12 * '\u2500',
      '\u252C', 12 * '\u2500', '\u2510', sep='')
print('\u2502', '  ', 'i  ', '\u2502', 4 * ' ', 'z', 5 * ' ', '\u2502', 3 * ' ', 'f1', 5 * ' ',
      '\u2502', 4 * ' ', 'f2', 4 * ' ', '\u2502', sep='')
print('\u251C', 6 * '\u2500', '\u253C', 11 * '\u2500', '\u253C', 12 * '\u2500',
      '\u253C', 12 * '\u2500', '\u2524', sep='')

for i in range(n):
    z = z + sh
    f1 = z * log(z) + 0.125
    f2 = 3 * z - exp(z)
    y[i] = round(f2, 2)
    x[i] = round(z, 2)
    if f2 > maxf2:
        maxf2 = f2
    if f2 < minf2:
        minf2 = f2
    print('\u2502', '{:3d}'.format(i), '\u2502', '{:8.2f}'.format(z), '\u2502',
          '{:8.2f}'.format(f1), '\u2502', '{:8.2f}'.format(f2), '\u2502')

print('\u2514', 6 * '\u2500', '\u2534', 11 * '\u2500', '\u2534', 12 * '\u2500',
      '\u2534', 12 * '\u2500', '\u2518', sep='')

print('Минимальное значение функции f2 = \t', '{:4.2f}'.format(minf2))
print('Максимальное значение функции f2 = \t', '{:4.2f}'.format(maxf2))

print('График f2')
l = 60
maxy = max(y)
miny = min(y)
if max(y) < 0:
    maxy = 0
if min(y) > 0:
    miny = 0
mo = int(abs((-miny) * l / (maxy - miny)))
if 0 in x:
    for i in range(len(x)):
        m = int(abs((y[i] - miny)  / (maxy - miny)))

        if x[i] == 0:
            if m == mo:
                print('{:5.10f}'.format(x[i]), '  ', (m + 3) * '\u2500', '*',
                      (l - m -1) * '\u2500', 'Y', sep='')
            elif m < mo:
                print('{:5.1f}'.format(x[i]), '  ', (m + 3) * '\u2500', '*',
                      (mo - m - 1) * '\u2500', '\u253C', (l - mo - 1) * '\u2500', 'Y', sep='')
            else:
                print('{:5.1f}'.format(x[i]), '  ', (mo + 3) * '\u2500', '\u253C',
                      (m - mo - 1) * '\u2500', '*', (l - m - 1) * '\u2500', 'Y', sep='')

        else:
            if m == mo:
                print('{:5.1f}'.format(x[i]), '  ', m * ' ', '*', (l - m - 1) * ' ', sep='')
            elif m < mo:
                print('{:5.1f}'.format(x[i]), '  ', m * ' ', '*',
                      (mo - m - 1) * ' ', '\u2502', sep='')
            else:
                print('{:5.1f}'.format(x[i]), '  ', mo * ' ', '\u2502',
                      (m - mo - 1) * ' ', '*', sep='')
    print((mo + 6) * ' ', 'X')

elif x[0] > 0:
    print('  0.0  ', mo * '\u2500', '\u253C', (70 - mo - 1 + 2) * '\u2500', 'Y', sep='')
    for i in range(len(x)):
        m = int(abs((y[i] - miny) * l / (maxy - miny)))
        if m == mo:
            print('{:5.1f}'.format(x[i]), '  ', m * ' ', '*', (l - m - 1) * ' ', sep='')
        elif m < mo:
            print('{:5.1f}'.format(x[i]), '  ', m * ' ', '*',
                  (mo - m - 1) * ' ', '\u2502', sep='')
        else:
            print('{:5.1f}'.format(x[i]), '  ', mo * ' ', '\u2502',
                  (m - mo - 1) * ' ', '*', sep='')
    print((mo + 6) * ' ', 'X')

else:
    for i in range(len(x)):
        m = int(abs((y[i] - miny) * l / (maxy - miny)))
        if m == mo:
            print('{:5.1f}'.format(x[i]), '  ', m * ' ', '*', (l - m - 1) * ' ', sep='')
        elif m < mo:
            print('{:5.1f}'.format(x[i]), '  ', m * ' ', '*',
                  (mo - m - 1) * ' ', '\u2502', sep='')
        else:
            print('{:5.1f}'.format(x[i]), '  ', mo * ' ', '\u2502',
                  (m - mo - 1) * ' ', '*', sep='')
    print('  0.0  ', mo * '\u2500', '\u253C', (70 - mo - 1 + 2) * '\u2500', 'Y', sep='')
    print((mo + 6) * ' ', 'X')
