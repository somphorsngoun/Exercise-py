# IMPORTS
import tkinter as tk
import random




#CONSTANTS
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

#VARIABLE
X = 0
Y = 0
# FUNCTIONS

def go():
    global X,Y
    X += 5
    Y += 5
    canvas.moveto(ball, X,Y)
    canvas.after(100, go)


#Main
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

#Create sharp
ball = canvas.create_oval(X, Y, X+50, Y+50, fill=random.choice(colors))
go()


# call the draw cicle after 5 seconds
root.mainloop()