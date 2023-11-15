import Camera
r = ["r","r","r","r","r","r","r","r","r"]
g = ["g","g","g","g","g","g","g","g","g"]
b = ["b","b","b","b","b","b","b","b","b"]
o = ["o","o","o","o","o","o","o","o","o"]
y = ["y","y","y","y","y","y","y","y","y"]
w = ["w","w","w","w","w","w","w","w","w"]

colors = [r,g,b,o,y,w]
algorithms = ["F U R U' R' F'","R U R' U R U2 R'","L' U R U' L U R' R U R' U R U2 R'","R U' R U R U R U' R' U' R2","L' U' L' U L' U L' U' L U L2"]
def O(f):
    if f == r:
        op = o
    elif f == o:
        op = r
    elif f == b:
        op = g
    elif f == g:
        op == b
    elif f == y:
        op == w
    elif f == w:
        op == y


def R():
    F = input("Enter the face")
    if F == "g":
        F = g
    elif F == "y":
        F = y
    elif F == "r":
        F = r
    elif F == "w":
        F = w
    elif F == "o":
        F = o
    elif F == "b":
        F = b
    p1 = F.copy()
    p2 = y.copy()
    p3 = o.copy()
    p4 = w.copy()
    p5 = g.copy()
    print(p2)
    r[2] = p4[8]
    r[5] = p4[5]
    r[8] = p4[2]
    y[2] = p1[2]
    y[5] = p1[5]
    y[8] = p1[8]
    o[2] = p2[8]
    o[5] = p2[5]
    o[8] = p2[2]
    w[2] = p3[2]
    w[5] = p3[5]
    w[8] = p3[8]
    g[0] = p5[6]
    g[1] = p5[3]
    g[2] = p5[0]
    g[3] = p5[7]
    g[5] = p5[1]
    g[6] = p5[8]
    g[7] = p5[5]
    g[8] = p5[2]
    
def Rp():
    
    p1 = r.copy()
    p2 = y.copy()
    p3 = o.copy()
    p4 = w.copy()
    p5 = g.copy()
    
    r[2] = p2[2]
    r[5] = p2[5]
    r[8] = p2[8]
    y[2] = p3[8]
    y[5] = p3[5]
    y[8] = p3[2]
    o[2] = p4[2]
    o[5] = p4[5]
    o[8] = p4[8]
    w[2] = p1[2]
    w[5] = p1[5]
    w[8] = p1[8]
    g[0] = p5[2]
    g[1] = p5[5]
    g[2] = p5[8]
    g[3] = p5[1]
    g[5] = p5[7]
    g[6] = p5[0]
    g[7] = p5[5]
    g[8] = p5[6]

def L():
    p1 = r.copy()
    p2 = y.copy()
    p3 = o.copy()
    p4 = w.copy()
    p5 = b.copy()
    print(p5)
    r[0] = p2[0]
    r[3] = p2[3]
    r[6] = p2[6]
    y[0] = p3[8]
    y[3] = p3[5]
    y[6] = p3[2]
    o[2] = p4[2]
    o[5] = p4[5]
    o[8] = p4[8]
    w[0] = p1[0]
    w[3] = p1[3]
    w[6] = p1[6]
    b[0] = p5[6]
    b[1] = p5[5]
    b[2] = p5[0]
    b[3] = p5[7]
    b[5] = p5[1]
    b[6] = p5[8]
    b[7] = p5[3]
    b[8] = p5[2]
def Lp():
    p1 = r.copy()
    p2 = y.copy()
    p3 = o.copy()
    p4 = w.copy()
    p5 = b.copy()
    r[0] = p4[0]
    r[3] = p4[3]
    r[6] = p4[6]
    y[0] = p1[0]
    y[3] = p1[3]
    y[6] = p1[6]
    o[2] = p2[6]
    o[5] = p2[3]
    o[8] = p2[6]
    w[0] = p3[0]
    w[3] = p3[3]
    w[6] = p3[6]
    b[0] = p5[2]
    b[1] = p5[3]
    b[2] = p5[8]
    b[3] = p5[7]
    b[5] = p5[1]
    b[6] = p5[0]
    b[7] = p5[5]
    b[8] = p5[6]
def U():
    p1 = r.copy()
    p2 = b.copy()
    p3 = o.copy()
    p4 = g.copy()
    p5 = y.copy()
    r[0] = p4[0]
    r[1] = p4[1]
    r[2] = p4[2]
    b[2] = p1[2]
    b[1] = p1[1]
    b[0] = p1[0]
    o[0] = p2[0]
    o[1] = p2[1]
    o[2] = p2[2]
    g[2] = p3[0]
    g[1] = p3[1]
    g[0] = p3[2]
    y[0] = p5[6]
    y[1] = p5[3]
    y[2] = p5[0]
    y[3] = p5[7]
    y[5] = p5[1]
    y[6] = p5[8]
    y[7] = p5[5]
    y[8] = p5[2]
def Up():
    p1 = r.copy()
    p2 = b.copy()
    p3 = o.copy()
    p4 = g.copy()
    p5 = y.copy()
    print(p5)
    r[0] = p2[0]
    r[1] = p2[1]
    r[2] = p2[2]
    b[2] = p3[0]
    b[1] = p3[1]
    b[0] = p3[2]
    o[0] = p4[0]
    o[1] = p4[1]
    o[2] = p4[2]
    g[0] = p1[0]
    g[1] = p1[1]
    g[2] = p1[2]
    y[0] = p5[2]
    y[1] = p5[5]
    y[2] = p5[8]
    y[3] = p5[1]
    y[5] = p5[7]
    y[6] = p5[3]
    y[7] = p5[0]
    y[8] = p5[6]
i = 0
while i == 0:
    m = input("Enter the move")
    if m == "R":
        R()
    elif m == "R'":
        Rp()
    elif m == "L":
        L()
    elif m == "L'":
        Lp()
    elif m == "U":
        U()
    elif m == "U'":
        Up()
    else:
        print(colors)
   
   

