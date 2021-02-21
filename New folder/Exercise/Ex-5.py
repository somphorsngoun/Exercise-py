# IMPORTS
import tkinter as tk
import random




#CONSTANTS
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

#VARIABLE
X = 200
Y = 200
# FUNCTIONS

def moveup(event):
    canvas.move(ball, 0,-10)
    print(True)

def movedown(event):
    print(True)
    canvas.move(ball, 0,10)

def moveleft(event):
    canvas.move(ball, -10,0)
    print(True)


def moveright(event):
    canvas.move(ball, 10,0)
    print(True)



#Main
root = tk.Tk()
root.geometry("1000x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

#Create sharp
ball = canvas.create_oval(X, Y, X+50, Y+50, fill=random.choice(colors))
canvas.bind(ball, "<Up>", moveup)
canvas.bind(ball, "<Down>", movedown)
canvas.bind(ball, "<Left>", moveleft)
canvas.bind(ball, "<Right>", moveright)


# call the draw cicle after 5 seconds
root.mainloop()