# IMPORTS
import tkinter as tk
import random




#CONSTANTS
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

#VARIABLE
X = 0
Y = 0
X1 = 550
Y1 = 0
X2 = 550
Y2 = 550
X3 = 0
Y3 = 550
IsFound = True
boo = False
IsFound1 = True
boo1 = False
IsFound2 = True
boo2 = False
IsFound3 = True
boo3 = False

# FUNCTIONS
def go3():
    global X3,Y3,IsFound3,boo3
    if boo3:
        X3 -= 5
        Y3 += 5
        if X3 == 0:
            IsFound3 = True
            boo3 = False
        
    if IsFound3:
        X3 += 5
        Y3 -= 5
        if X3 == 550:
            boo3 = True
            IsFound3 = False
    canvas.moveto(ball3, X3,Y3)
    canvas.after(50, go3)

def go2():
    global X2,Y2,IsFound2,boo2
    if boo2:
        X2 += 5
        Y2 += 5
        if X2 == 550:
            IsFound2 = True
            boo2 = False
        
    if IsFound2:
        X2 -= 5
        Y2 -= 5
        if X2 == 0:
            boo2 = True
            IsFound2 = False
    canvas.moveto(ball2, X2,Y2)
    canvas.after(50, go2)

def go1():
    global X1,Y1,IsFound1,boo1
    if boo1:
        X1 = X1 +5
        Y1 = Y1 -5
        if X1 == 550:
            IsFound1 = True
            boo1 = False
        
    if IsFound1:
        X1 -= 5
        Y1 += 5
        if X1 == 0:
            boo1 = True
            IsFound1 = False
    canvas.moveto(ball1, X1,Y1)
    canvas.after(50, go1)

def go():
    global X,Y,IsFound,boo
    if boo:
        X = X -5
        Y = Y -5
        if X == 0:
            IsFound = True
            boo = False
        
    if IsFound:
        X += 5
        Y += 5
        if X == 550:
            boo = True
            IsFound = False
    canvas.moveto(ball, X,Y)
    canvas.after(50, go)


#Main
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

#Create sharp
ball = canvas.create_oval(X, Y, X+50, Y+50, fill=random.choice(colors))
ball1 = canvas.create_oval(X1, Y1, X1+50, Y1+50, fill=random.choice(colors))
ball2 = canvas.create_oval(X2, Y2, X2+50, Y2+50, fill=random.choice(colors))
ball3 = canvas.create_oval(X3, Y3, X3+50, Y3+50, fill=random.choice(colors))
go()
go1()
go2()
go3()

# call the draw cicle after 5 seconds
root.mainloop()