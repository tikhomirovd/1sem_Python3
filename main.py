 # Вычислить интеграл методом левых прямоугольников и параболы

from math import pi, sin, e

a = 0  # Левый край
b = pi  # Правый край
n = 100  # Количество итераций


def print_header():
    print('Итерация\tПлощадь')


def print_table(n, s):
    print(f'\t{n}\t\t{s:.4f}')


def f(x):
    return e * sin(x)


def left_rectangle(f, a, b, n):
    print_header()
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h)
        print_table(i, s)
    s *= h
    return s


def parabola(f, a, b, n):
    print_header()
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h) + 4 * f(a + i * h + h / 2) + f(a + i * h + h)
        print_table(i, s)
    s *= h / 6
    return s


LR = left_rectangle(f, a, b, n)
print()
print(f'Методом левых прямоугольников: {LR:.4f}')

print()

P = parabola(f, a, b, n)
print()
print(f'Методом параболы: {P:.4f}')
