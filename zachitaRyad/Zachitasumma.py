from math import factorial
x = float(input('Введите начальное значение '))
eps = float(input('Введите точность Eps '))

a = 1
b = - 4 * x ** 2 / 2
sum = a
i = 0

while abs(b - a) > eps:
    i += 1
    i2 = i * 2
    i21 = i * 2 - 2
    b = (-1) ** i * (2 * x) ** i2 / factorial(i2)
    a = ((-1) ** (i - 1)) * ((2 * x) ** i21) / factorial(i21)
    sum += b
    print('Сумма заданного ряда на', i, 'итерации', 'равна',  '{:5.8f}'.format(sum))
print('Сумма заданного ряда равна ', '{:5.8f}'.format(sum))
