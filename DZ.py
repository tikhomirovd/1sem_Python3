r = float(input('Введите начальное значение '))
k = float(input('Введите конечное значение '))
sh = float(input('Введите шаг '))
count = 0
n = int((abs(k - r)) / abs(sh) + 1)
y = n * [0]
x = n * [0]
r = r - sh
c = ' '

print('\u250C', 5 * '\u2500', '\u252C', 10 * '\u2500', '\u252C', 12 * '\u2500',
       8 * '\u2500', '\u2510', sep='')
print('\u2502', '  ', 'N  ', '\u2502', 4 * ' ', 'z', 5 * ' ', '\u2502', 3 * ' ', 'f1', 15 * ' ',
      '\u2502', sep='')
print('\u251C', 5 * '\u2500', '\u253C', 10 * '\u2500', '\u253C', 13 * '\u2500',
       7 * '\u2500', '\u2524', sep='')


for i in range(n):
    r = r + sh
    f2 = (r * (r * (r * (r * (r * 1) - 7.9)  + 24.46) - 37.074) + 27.512) - 8.0042
    y[i] = round(f2, 2)
    x[i] = round(r, 2)
    print('\u2502', '{:3d}'.format(i), '\u2502', '{:8.2f}'.format(r), '\u2502',
          '{:12.2f}'.format(f2),  '      \u2502')

print('\u2514', 5 * '\u2500', '\u2534', 10 * '\u2500', '\u2534', 12 * '\u2500',
       8 * '\u2500', '\u2518', sep='')


print('График f1')
l = 60
maxy = max(y)
miny = min(y)
print('Максимальное значение равно', maxy)
print('Минимальное значение равно', miny)

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
                print('{:5.10f}'.format(x[i]), '  ', m * '\u2500', '*',
                      (l - m - 1) * '\u2500', 'Y', sep='')
            elif m < mo:
                print('{:5.1f}'.format(x[i]), '  ', m * '\u2500', '*',
                      (mo - m - 1) * '\u2500', '\u253C', (l - mo - 1) * '\u2500', 'Y', sep='')
            else:
                print('{:5.1f}'.format(x[i]), '  ', mo * '\u2500', '\u253C',
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
    print('  0.0  ', mo * '\u2500', '\u253C', (70 - mo - 1) * '\u2500', 'Y', sep='')
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
    print('  0.0  ', mo * '\u2500', '\u253C', (70 - mo - 1) * '\u2500', 'Y', sep='')
    print((mo + 6) * ' ', 'X')
