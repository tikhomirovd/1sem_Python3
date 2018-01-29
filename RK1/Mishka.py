from math import exp, log

e = float(input("Введите эпсилон "))
x = float(input('Введите значение логарифма '))
mod = 0
if x <= 0:
    print('Аргумент логарифма должен быть положительный ')
else:
    logx = log(x)
    n = 1
    S = 0
    while abs(logx - S) > e:
        if n + 1 % 2 == 0:
            mod = 1
        else:
            mod = -1
        S = S + mod * (exp((n - 1) * log(x)) / n)
        n = n + 1
    print('Значение логарифма по ряду равно ' , S)
    print('Точное значение логарифма равно ', logx)
    a = abs(logx - S)
    print('Абсолютная погрешность = ', a)


