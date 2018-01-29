from math import factorial
x = float(input('Введите начальное значение '))
eps = float(input('Введите точность Eps '))

a = x
b = x ** 3 / factorial(3)
sum = a
i = 0

while abs(b - a) > eps:
    i += 1
    i2 = i * 2 + 1
    i21 = i * 2 - 1
    b = x ** i2 / factorial(i2)
    a = x ** i21 / factorial(i21)
    sum += b
    print('Сумма заданного ряда на', i, 'итерации', 'равна',  '{:5.8f}'.format(sum))
print('Сумма заданного ряда равна ', '{:5.8f}'.format(sum))
