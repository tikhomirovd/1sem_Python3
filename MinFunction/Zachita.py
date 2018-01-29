a = float(input('Введите a '))
b = float(input('Введите b '))
alpha = float(input('Введите шаг '))
l = 60
n = int(abs(b -a) / abs(alpha) + 1)
y = n * [0]
x = n * [0]

for i in range(n):
    f1 = a * a - 36
    y[i] = round(f1, 2)
    x[i] = round(a, 2)
    a += alpha
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
