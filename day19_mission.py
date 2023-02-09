from tkinter import *


def draw(x, y, sz) :
	if sz >= 30 :
		draw(x, y, sz / 2)
		draw(x + sz / 2, y, sz / 2)
		draw(x + sz / 4, int(y - sz * (3 ** 0.5) / 4), sz / 2)
	else :
		canvas.create_polygon (x, y, x + sz, y, x + sz / 2, y - sz * (3 ** 0.5) / 2, fill ='red', outline ="red")


ws = 1000
rd = 400


window = Tk()
window.title("삼각형 모양의 프랙탈")
canvas = Canvas(window, height = ws, width = ws, bg ='white')

draw(ws / 5, ws / 5 * 4, ws * 2 / 3)

canvas.pack()
window.mainloop()
