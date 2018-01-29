from math import pi, sin, cos
from random import random

def f(x):
    return sin(x)

def leftRect(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)
    s *= h
    return s

def rightRect(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(1,n+1):
        s += f(a+i*h)
    s *= h
    return s

def middleRect(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h+h/2)
    s *= h
    return s

def trapeze(f,a,b,n):
    s = (f(a)+f(b))/2
    h = (b-a)/n
    for i in range(1,n):
        s += f(a+i*h)
    s *= h
    return s

def parabola(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)+4*f(a+i*h+h/2)+f(a+i*h+h)
    s *= h/6
    return s

def Newton(f,a,b,n): # метод 3/8
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)+3*f(a+i*h+h/3)+3*f(a+i*h+2*h/3)+f(a+i*h+h)
    s *= h/8
    return s


def Boole(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += 7*f(a+i*h)+32*f(a+i*h+h/4)+12*f(a+i*h+h/2)+\
        32*f(a+i*h+3*h/4)+7*f(a+i*h+h)
    s *= h/90
    return s

def Weddle(f,a,b,n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)+5*f(a+i*h+h/6)+f(a+i*h+h/3)+\
        6*f(a+i*h+h/2)+\
        f(a+i*h+2*h/3)+5*f(a+i*h+5*h/6)+f(a+i*h+h)
    s *= h/20
    return s

def MonteCarlo(f,a,b,minf,maxf,n):
    k = 0
    for i in range(n):
        x = random()*(b-a)+a
        y = random()*(maxf-minf)+minf
        F = f(x)
        if y>=0 and y<=F:
            k += 1
        elif y<0 and y>=F:
            k -= 1
    return (b-a)*(maxf-minf)*k/n

a = 0
b = pi/2
n = 100
I = leftRect(f,a,b,n)
print(I)
I = rightRect(f,a,b,n)
print(I)
I = middleRect(f,a,b,n)
print(I)
I = trapeze(f,a,b,n)
print(I)
I = parabola(f,a,b,n)
print(I)
I = Newton(f,a,b,n)
print(I)
I = Boole(f,a,b,n)
print(I)
I = Weddle(f,a,b,n)
print(I)
I = MonteCarlo(f,a,b,0,1,n)
print(I)
