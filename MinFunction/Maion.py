# Данная программа считает значение заданной функции
# При заданных аргументах
# Вычисляет минимум и максимум функции
# Строит таблицу значений и рисует график функции

# Тихомиров Дмитрий

# z0, z1 - начальное и конечное значение функций
# step - шаг, с которым идёт функция
# a, b, c, cherta, rr, rrb, rrd - символы юникода
# PL3, PL4, PL5, PL6, PL7, PL30 - символьные строки
# f1, f2 - значение функции
# maximum, minimum - максимальное и минимальное значени функции
# maximumNum - Номер , при котором функция принимает максимальое значение
# ymaxgr, ymingr - границы оси Y
# count - количество  повторений
# Num, i  -  счетчик
# xp, yp - координаты в построенной плоскости
# oc - существование оси X



from math import log, exp, e

maximum = -10000
minimum = 100000
maximumNum = -10000
ymaxgr = 0
ymingr = 0


# Символы юникода
w = '\u02cd'
er = '\u00A6'
r = '\u02C9'
vert = '\u2502'
rr = '\u2534'
rrd = '\u252c'
rrb = '\u2500'
PL0 = 56 * w
PL1 = er + r * 5 + er + r*10 + er + r*13 + er + r * 12 + er
PL1 = 56 * r
PL3 = rr + 15 * rrb + rr + 13 * rrb + rrd + rrb + rr + 15 * rrb + rr + 12 * rrb
PL30= rr + 15 * rrb + rr + 15 * rrb + rr + 15 * rrb + rr + 12 * rrb
PL7 = ' '*25
print()

print(PL1)






# Вводим значения и вычисляем шаг
z0 = float(input('Введите начальное значение Z '))
z1 = float(input('Введите конечное значение Z '))
step = float(input('Введите шаг функции '))
count = int((z1 - z0) / step) + 1

print(PL0)
print(er, ' \tN\t ', er, '   \tZ\t', er, '   \tF1\t\t ', er, '      F2      ', er)


# Строим шапку таблицы




# Вычисляем значения функции на промежутке и находим максимальный аргумент
for Num in range(count):
    f1 = z0 * log(z0) + 0.125
    f2 = 3 * z0 - exp(z0)
    if maximum < f2:
        maximum = f2
        maximumNum = Num
    if minimum > f2:
        minimum = f2

    print(PL1)
    print(er, Num + 1, '\t ', er, '{:1.2f}'.format(z0), '\t', er,
          '{:1.3e}'.format(f1), '\t ',er, '{:1.2e}'.format(f2), '\t  ',er)
    z0 += step

print()
print('Максимальный элемент функции f2 равен ', '{:e}'.format(maximum))
print('Значение Z, при котором значение f2 максимально равно ', maximumNum)
print('\nМинимальное значение f2: {:.4f}'.format(minimum))
print('Максимальное значение f2: {:.4f}'.format(maximum))


# Проверка на существование оси X
if maximum < 0 or minimum > 0:
    oc = False
else:
    oc = True

if oc:
    if abs(maximum) > abs(minimum):
        ymaxgr = maximum
        ymingr = -1 * ymaxgr
    else:
        ymaxgr = abs(minimum)
        ymingr = minimum
else:
    ymaxgr= maximum
    ymingr = minimum

zn1 = ymingr
zn2 = 16 / 60 * (ymaxgr - ymingr) + ymingr
zn3 = 32 / 60 * (ymaxgr - ymingr) + ymingr
zn4 = 48 / 60 * (ymaxgr - ymingr) + ymingr
#print('\n\t\t{:1.3e}\t{1.3e}\t{1.3e}\t.{1.3e}'.format(zn1, zn2, zn3, zn4), sep='')


if oc:
    print('\n\t\tX\t', PL3, 'Y', sep='')
else:
    print('\n\t\tX\t', PL30, 'Y', sep='')



for i in range(count):
    f2 = 3 * z0 - exp(z0)
    yp = (f2 - ymingr) / (ymaxgr - ymingr)
    yp = round(yp*40)
    xp = z0 + i * step
    print(' {:1.3e}\t'.format(xp), sep='', end = '')
    if oc:
        if f2 < 0 and yp != 25:
            PL4 = ' '*yp
            PL5 = ' ' * (24 - yp)
            print(PL4, '*', PL5, vert, sep=' ')
        elif f2 > 0 and yp != 25:
            PL5 = ' ' * (yp - 26)
            print(PL7, vert, PL5, '*', sep='')
        else:
            print(PL7, '*', sep='')
    else:
        if f2 < 0:
            PL6 = ' '*yp
            print(PL6, '*', sep='')
        elif f2 > 0:
            PL6 = ' '*yp
            print(PL6, '*', sep = '')
    z0 += step
if oc:
    print('\t\t', PL7, '    X', sep='')



