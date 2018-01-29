a = float(input('Введите начальное значение '))
b = float(input('Введите конечное значение '))
c = float(input('Введите шаг '))
q = int((b - a)/c) + 1
ymax = a * a - 36
ymin = a * a - 36

for i in range(1, q):
    x = a + i * c
    y = x * x - 36
    ymax = max(ymax, y)
    ymin = min(ymin, y)

zn = int(-ymin*60/(ymax - ymin))
print('\t\t', '_'*61, ' Y', sep = "")

for i in range(q):
    x = a + i*c
    y = x * x - 36
    yp = int(60 * ( y - ymin) / (ymax - ymin))
    print('{:1.3f}\t'.format(x), end='', sep='')

    if ymax < 0 or ymin > 0:
        print(' '*(yp - 1), '*', sep ='')
    else:
        if zn > yp:
            print(' '*yp, '*', ' '*(zn - yp - 1), '\u2502', sep ='')
        elif zn < yp:
            print(' '*zn, '\u2502', ' '*(yp - zn - 1), '*', sep ='')
        else:
            print(' '*(yp - 1), '*')












