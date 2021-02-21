# IMPORTS
import tkinter as tk
import random


#CONSTANTS
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

#VARIABLE
X = 0
Y = 0
boo = True
boos = False
A = False
# FUNCTIONS

def go():
    global X,Y,boo,boos,A
    if boo:
        X += 10
        Y += 5
        if Y == 525:
            boo = False
            boos = True
        
    if boos:
        X -= 10
        Y -= 5
        if 0 == Y:
            boo = True
            boos = False

    canvas.moveto(ball, X,Y)
    canvas.after(50, go)

def moveLeft(event):
    canvas.move(play, -30,0)
    if X == event.y:
        X += 20 

def moveRight(event):
    canvas.move(play, 30,0)


#Main
root = tk.Tk()
root.geometry("1000x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

#Create sharp
ball = canvas.create_oval(X, Y, X+50, Y+50, fill=random.choice(colors))

play = canvas.create_rectangle(270, 570, 400, 600, fill=random.choice(colors))
canvas.bind("<Button-1>", moveLeft)
canvas.bind("<Button-3>", moveRight)
go()


# call the draw cicle after 5 seconds
root.mainloop()