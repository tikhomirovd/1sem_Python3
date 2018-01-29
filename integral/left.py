def f(x):
    return x

def leftRect(f,a,b,n):
    s = 0
    s1 = 0
    z = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)
        s1 += f(a+2*i*h)
        z += 1
        if abs(s1 - s) > e:
            break
    s *= h
    if z == n:
        print('Ряд1 не сошёлся')
    else:
        print('Ряд1 сошёлся, интеграл равен', '{:f}'.format(s),
              'за', z, 'шагов')
    return s

def trapeze(f,a,b,n):
    z = 0
    s = (f(a)+f(b))/2
    s1 = 0
    h = (b-a)/n
    for i in range(1,n):
        s += f(a+i*h)
        s += f(a + 2* i * h)
        if abs(s1 - s) > e:
            break
    s *= h
    if z == n:
        print('Ряд3 не сошёлся')
    else:
        print('Ряд3 сошёлся, интеграл равен', '{:f}'.format(s),
              'за', z, 'шагов')
    return s

def parabola(f,a,b,n):
    s = 0
    s1 = 0
    z = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)+4*f(a+i*h+h/2)+f(a+i*h+h)
        s1 += f(a + 2*i * h) + 4 * f(a + 2*i * h + h / 2) + f(a + 2*i * h + h)
        z += 1
        if abs(s1 - s) > e:
            break
    s *= h/6
    if z == n:
        print('Ряд2 не сошёлся')
    else:
        print('Ряд2 сошёлся, интеграл равен', '{:f}'.format(s),
              'за', z, 'шагов')
    return s
e = float(input('Введите эпсилон '))
a = 0
b = 1
n = 1000
leftRect(f,a,b,n)
parabola(f,a,b,n)



trapeze(f,a,b,n)
