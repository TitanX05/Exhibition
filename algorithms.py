import Camera
from tkinter import *
from tkinter import ttk
import numpy as np


faces = np.array_split(Camera.color, 6)
print(faces)
r = faces[0]
g = faces[1]
o = faces[2]
b = faces[3]
y = faces[4]
w = faces[5]
p1 = y.copy()
p2 = r.copy()
p3 = b.copy()
p4 = o.copy()
p5 = g.copy()
p6 = w.copy()


def oll():
    if y[1] == "y" and y[3] == "y" and y[5] == "y" and y[7] == "y" and (y != p1).all:
        if (y[2] == "y" and y[8] == "y" and r[0] == "y" and o[2] == "y") or (y[6] == "y" and y[8] == "y" and b[0] == "y" and g[2] == "y"):
            return("L F R'F'L'F R F'")

        elif (y[1] == "y" and y[3] == "y" and y[5] == "y" and y[6] == "y" and y[7] == "y"
              and r[2] == "y") or (y[0] == "y" and y[1] == "y" and y[3] == "y" and y[5] == "y"
                                   and y[7] == "y" and b[2] == "y") or (y[1] == "y" and y[2] == "y" and
                                                                        y[3] == "y" and y[5] == "y" and y[7] == "y"
                                                                        and o[2] == "y") or (y[1] == "y" and y[3] == "y" and y[5] == "y" and y[7] == "y" and y[8] == "y"
                                                                                             and r[2] == "y"):
            return("R U R' U R U2 R' ")

        elif (r[0] == "y" and r[2] == "y" and o[0] == "y" and o[2] == "y") or (g[0] == "y" and g[2] == "y" and b[0] == "y" and b[2] == "y"):
            return("F R U R' U' R U R' U' R U R' U'")

        elif (y[0] == "y" and y[8] == "y" and y[2] != "y" and y[6] != "y") or (y[2] == "y" and y[6] == "y" and y[0] != "y" and y[8] != "y"):
            return("Hold as shown above and do the algorithm : \n R' F R B' R'F' R B")

        elif (y[8] == "y" and r[0] == "y" and o[2] != "y") or (y[6] == "y" and b[0] == "y" and g[2] != "y") or (y[0] == "y" and o[0] == "y" and r[2] != "y") or (y[2] == "y" and g[0] == "y" and b[2] != "y"):
            return("L' U' L U' L' U U L")

        elif (r[0] == "y" and r[2] == "y" and g[2] == "y" and b[0] == "y") or (b[0] == "y" and b[2] == "y" and r[2] == "y" and o[0] == "y") or (g[0] == "y" and g[2] == "y" and o[2] == "y" and r[0] == "y") or (o[0] == "y" and o[2] == "y" and b[2] == "y" and g[0] == "y"):
            return("Hold as shown above and do the algorithm : \n R U U R R U' R R U' R R U U R")

        elif (r[0] == "y" and r[2] == "y" and y[0] == "y") or (b[0] == "y" and b[2] == "y" and y[2] == "y") or (o[0] == "y" and o[2] == "y" and y[8] == "y") or (g[0] == "y" and g[2] == "y" and y[6] == "y"):
            return("R2 D R' U2 R D' R' U2 R'")
        else:
            return("Error")


def pll1():

    if (y == p1).all and r[0] == "r" and r[2] == "r" and g[0] == "g" and g[2] == "g" and o[0] == "o" and o[2] == "o" and b[0] == "b" and b[2] == "b":

        if (r[0] == "r" and r[1] == "r" and r[2] == "r" and b[1] == "g") or (b[0] == "b" and b[1] == "b" and b[2] == "b" and o[1] == "r") or (g[0] == "g" and g[1] == "g" and g[2] == "g" and r[1] == "o") or (o[0] == "o" and o[1] == "o" and o[2] == "y" and g[1] == "b"):
            return("R U' R U R U R U' R' U' R R")

        elif (r[0] == "r" and r[1] == "r" and r[2] == "r" and g[1] == "b") or (b[0] == "b" and b[1] == "b" and b[2] == "b" and r[1] == "o") or (g[0] == "g" and g[1] == "g" and g[2] == "g" and o[1] == "r") or (o[0] == "o" and o[1] == "o" and o[2] == "y" and b[1] == "g"):
            return("L' U L' U' L' U' L' U L U L L")

        elif r[1] == "o" and o[1] == "r" and b[1] == "g" and g[1] == "b":
            return("M2 U M2 U2 M2 U M2")

        elif (r[1] == "g" and g[1] == "r") or (g[1] == "o" and o[1] == "g"):
            return(" M U M2 U M2 U M U2 M2 U'")
        else:
            return("Error")


# def pll2():
#     # print(r)
#     # print(b)
#     # print(g)
#     # print(o)
#     if (r[0] == "r" and r[1] == "r" and r[2] == "r") or (b[0] == "b" and b[1] == "b" and b[2] == "b") or (g[0] == "g" and g[1] == "g" and g[2] == "g") or (o[0] == "o" and o[1] == "o" and o[2] == "y"):
#         return("L' U R U' L U U R' U R U U R'")
#     else:
#         return("F R U' R' U' R U R' F' R U R' U' R' F R F'")


print("Running happened")
root = Tk()
root.geometry("180x80")
root.title("Algorithms")
a = oll()
b = pll1()
#c = pll2()
frm = ttk.Frame(root)
frm['padding'] = 10
frm.grid()
ttk.Label(frm, text = a).grid(column=0, row=0)
ttk.Label(frm, text= b).grid(column=0, row=10)
# ttk.Label(frm,text = c).grid(column=00, row=20)
#ttk.Label(frm, textvariable=c).grid(column=20, row=20)
root.mainloop()
print("Running happened")