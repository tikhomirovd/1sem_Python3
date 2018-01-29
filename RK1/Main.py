from math import sqrt

Ax, Ay = map(float, input('Введите координаты точки A через пробел ').split())
Bx, By = map(float, input('Введите координаты точки B через пробел ').split())
Cx, Cy = map(float, input('Введите координаты точки С через пробел ').split())
x, y = map(float, input('Введите координаты точки ').split())

ax, ay = Bx - Ax, By - Ay
bx, by = Cx - Bx, Cy - By
cx, cy = Ax - Cx, Ay - Cy

lenAB = sqrt(ax ** 2 + ay ** 2)
lenBC = sqrt(bx ** 2 + by ** 2)
lenCA = sqrt(cx ** 2 + cy ** 2)

atx, aty = x - Ax, y - Ay
btx, bty = x - Bx, y - By
ctx, cty = x - Cx, y - Cy

lenAT = sqrt(atx ** 2 + aty ** 2)
lenBT = sqrt(btx ** 2 + bty ** 2)
lenCT = sqrt(ctx ** 2 + cty ** 2)

pabt = (lenAB + lenAT + lenBT) / 2
pbtc = (lenBC + lenBT + lenCT) / 2
pcta = (lenCA + lenCT + lenAT) / 2

Sabt = sqrt(pabt * (pabt - lenAB) * (pabt - lenAT) * (pabt - lenBT))
Sbtc = sqrt(pbtc * (pbtc - lenBC) * (pbtc - lenBT) * (pbtc - lenCT))
Scta = sqrt(pcta * (pcta - lenCA) * (pcta - lenCT) * (pcta - lenAT))

Habt = 2 * Sabt / lenAB
Hbtc = 2 * Sbtc / lenBC
Hcta = 2 * Scta / lenCA

Hmax = max(Habt, Hbtc, Hcta)
print('Расстояние до наиболее удаленной стороны = ', '{:f}'.format(Hmax))