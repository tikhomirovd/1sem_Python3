# Данная программа определяет, существует ли треугольник с такими кооринатами
# Если треугольник существует, то находит длины его сторон
# Находит высоту, проведённую  из наименьшего угла треугольника
# Определяет, находится ли введёная точка внутри треугольника или нет
# И считает расстояние от этой точки о ближайшей стороны

# Тихомиров Дмитрий ИУ7-15Б

# Ax, Ay - координаты точки A на плоскости
# Bx, By - координаты точки В на плоскости
# Cx, Cy - координаты точки С на плоскости

# ax, ay - координаты прямой AB на плоскости
# bx, by - координаты прямой BC на плоскости
# cx, cy - координаты прямой CA на плоскости

# lenAB, lenBC, lenCA - длины сторон треугольника
# lenmin - Минимальная длина треугольника
# pabc - полупериметр треугольника ABC
# hmin - искомая высота
# Sabc - площадь треугольника ABC
# x, y - координаты, которые надо проверить

# atx, aty - координаты прямой AT на плоскости
# btx, bty - координаты прямой BT на плоскости
# ctx, cty - координаты прямой CT на плоскости

# lenAT, lenBT, lenCT - длины сторон AT, BT, CT
# Sabt, Sbtc, Satc - площади треугольников ABT, BTC, ATC
# pabt, pbtc, patc - полупериметры тругольникoв ABT, BTC, ATC
# hAB, hAC, hBC - высоты в  ABT, BTC, ATC , проведенные к основанию
# minSpace - минимальное расстояние от точки до стороны треугольника

from math import sqrt

Ax, Ay = map(float, input('Введите координаты точки А через пробел ').split())
Bx, By = map(float, input('Введите координаты точки B через пробел ').split())
Cx, Cy = map(float, input('Введите координаты точки С через пробел ').split())

# Вычисляем координаты длин прямых AB, BC, CA
ax, ay = Bx - Ax, By - Ay
bx, by = Cx - Bx, Cy - By
cx, cy = Ax - Cx, Ay - Cy

# Находим длины прямых AB, BC, CA
lenAB = sqrt(ax ** 2 + ay ** 2)
lenBC = sqrt(bx ** 2 + by ** 2)
lenCA = sqrt(cx ** 2 + cy ** 2)

print('Длина стороны AB равна ', '{:f}'.format(lenAB))
print('Длина стороны BC равна ', '{:f}'.format(lenBC))
print('Длина стороны CA равна ', '{:f}'.format(lenCA))

# По теореме о существовании треугольника проверяем данный треугольник
if lenAB + lenBC <= lenCA or lenBC + lenCA <= lenAB or lenCA + lenAB <= lenBC:
    print('Данный треугольник не существует ')
    if lenAB + lenBC == lenCA or lenBC + lenCA == lenAB or\
                            lenCA + lenAB == lenBC:
        print('Стороны лежат на одной прямой')
    else:
        print('Не выполняется неравенство треуольника ')
else:
    print('Треугольник существует')

    # Находим по формуле искомую высоту
    pabc = (lenAB + lenBC + lenCA) / 2
    Sabc = sqrt(pabc * (pabc - lenAB) * (pabc - lenBC) * (pabc - lenCA))
    lenmin = min(lenAB, lenBC, lenCA)
    hmin = 2 * Sabc / lenmin
    print('Высота треугольника равна ', '{:f}'.format(hmin))

    # Проверяем равенство сторон
    if (lenAB == lenBC) or (lenBC == lenCA) or (lenAB == lenCA):
        print('Треугольник является равнобедренным ')
    else:
        print('Треугольник не является равнобедренным ')

    x, y = map(float, input('Введите координаты точки на проверку ').split())

    # Находим координаты прямых AT, BT, CT
    atx, aty = x - Ax, y - Ay
    btx, bty = x - Bx, y - By
    ctx, cty = x - Cx, y - Cy

    # Находим длины прямых AT, BT, CT
    lenAT = sqrt(atx ** 2 + aty ** 2)
    lenBT = sqrt(btx ** 2 + bty ** 2)
    lenCT = sqrt(ctx ** 2 + cty ** 2)

    # Находим полупериметры и площади треугольников ABT, BTC, ATC
    pabt = (lenAB + lenBT + lenAT) / 2
    pbtc = (lenBC + lenBT + lenCT) / 2
    patc = (lenCA + lenAT + lenCT) / 2

    Sabt = sqrt(pabt * (pabt - lenAB) * (pabt - lenBT) * (pabt - lenAT))
    Sbtc = sqrt(pbtc * (pbtc - lenBC) * (pbtc - lenBT) * (pbtc - lenCT))
    Satc = sqrt(patc * (patc - lenCA) * (patc - lenCT) * (patc - lenAT))

    Sabt = round(Sabt, 1)
    Sbtc = round(Sbtc, 1)
    Satc = round(Satc, 1)
    Sabc = round(Sabc, 1)

    if Sabt + Sbtc + Satc == Sabc:
        print('Точка лежит внутри треугольника ')
    else:
        print('Точка лежит вне треугольника ')

    # Находим высоты в треугольниках, образованных через точку x,y
    hAB = 2 * Sabt / lenAB
    hBC = 2 * Sbtc / lenBC
    hAC = 2 * Satc / lenCA

    minSpace = min(hAB, hBC, hAC)
    print('Расстояние до ближайшей прямой равно ', '{:f}'.format(minSpace))













