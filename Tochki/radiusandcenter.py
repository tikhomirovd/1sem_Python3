import random
from math import sqrt

import tkinter as tk
n = 10
pointF = [0] * n
points = [0] * n
d = n
X = Y = R = z = c = v = 0
pIn = 0
pOut = 0


root = tk.Tk()

for i in range(n):
    points[i] = random.randrange(-50,50,1), random.randrange(-50,50,1)
    print(points[i])



def fx(x1, x2, x3, y1, y2, y3):
    k1 = x1 - x2
    k2 = - x1 - x2
    k3 = y2 - y1
    l1 = x2 - x3
    l2 = - x2 - x3
    l3 = y3 - y2
    temp = k1 * k2 / k3 - l1 * l2 / l3 + y2 - y3
    temp1 = 2 * l1 / l3 - 2 * k1 / k3
    d = temp / temp1
    return d

def fy(x1, x2, y1, y2, x):
    d = ((x1 - x2) * (2 * x - x1 - x2) / (y2 - y1) + y1 + y2) / 2
    return d

def r(x, y, x1, y1):
    return sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))

for i in range(n):
    for j in range(i + 1 , n):
        if points[i] == points[j]:
            continue
        for k in range(j + 1, n):
            if points[i] == points[k] or points[j] == points[k]:
                continue
            x = fx(points[i][0],points[j][0],points[k][0],
                   points[i][1], points[j][1], points[k][1])
            y = fy(points[i][0], points[j][0],
                   points[i][1], points[j][1], x)
            radius = r(x, y, points[j][0], points[j][1])
            for l in range(n):
                if l != i and l != j and l != k:
                    if r(x, y, points[j][0], points[j][1]) > radius:
                        pOut += 1
                    else:
                        pIn +=1
            if (abs(pIn - pOut) < d) or (abs(pIn - pOut) == d and R > radius):
                d = abs(pIn - pOut)
                X = x
                Y = y
                R = radius
                z = i
                c = j
                v = k
print(X, Y, R)



