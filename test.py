from tkinter import *
from tkinter import ttk;
import algorithms
root = Tk()
a = StringVar
a.set = algorithms.oll()
b = StringVar
b.set =  algorithms.pll1()
c = StringVar
c.set = algorithms.pll2()
frm = Tk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=a).grid(column=0, row=0)
ttk.Label(frm, text=b).grid(column=10, row=10)
ttk.Label(frm, text=c).grid(column=20, row=20)
root.mainloop()