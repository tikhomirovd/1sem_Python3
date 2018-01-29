from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()
step = int(input("Введите расстояние "))
p = [145, 145, 155, 155]
iters = 0
canvas.create_arc(*p, start=0, extent=200, style=ARC)

while p[0] > step:
    p[1] -= step/2  # расширение вниз
    p[3] += step/2  # расширение вверх

    if iters % 2:
        p[0] -= step  # расширение и сдвиг левой границы влево
        canvas.create_arc(*p, start=0, extent=180, style=ARC)
    else:
        p[2] += step  # расширение и сдвиг правой границы вправо
        canvas.create_arc(*p, start=0, extent=-180, style=ARC)

    iters += 1

root.mainloop()