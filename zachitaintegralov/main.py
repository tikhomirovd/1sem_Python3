# Тихомиров Дмитрий
# ИУ7-15Б

def f(x):
    # return 3 * x ** 3 + 2 * x ** 2 + 1
    return x*x*x*x*x*x*x

def Newton(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)+3*f(a+i*h+h/3)+3*f(a+i*h+2*h/3)+f(a+i*h+h)
    s *= h/8
    return s

a = 0
b = 1
n = 1
I = Newton(f,a,b,n)
print('Интеграл равен ', I)
