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
IsFound = True
boo = False
IsFound1 = True
boo1 = False
# FUNCTIONS
def move():
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
    canvas.after(50, move)

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
go()
move()

# call the draw cicle after 5 seconds
root.mainloop()