# IMPORTS
import tkinter as tk
import random




#CONSTANTS
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

#VARIABLE
X = 0
Y = 0
IsFound = True
boo = False
# FUNCTIONS

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
        if X == 600:
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
go()


# call the draw cicle after 5 seconds
root.mainloop()