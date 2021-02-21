# IMPORTS
import tkinter as tk
import random

#CONSTANTS
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

#VARIABLE

# FUNCTIONS
def remove():
    canvas.delete("text")

def clickOn(event):
    canvas.delete("go")
    canvas.create_text(event.x, event.y, fill="darkblue",font="Times 10 italic bold",text="good", tags="text")
    canvas.after(1000, remove)

def go():
    canvas.move("go", 0,20)
    canvas.tag_bind("go","<Button-1>", clickOn)

def drawRandomCircle():
    randomcolor = random.choice(colors)
    X1 = random.randrange(0,600)
    canvas.create_oval(X1, 0, X1+50, 50, fill=randomcolor, tags="go")
    canvas.after(100, go)
    canvas.after(500, drawRandomCircle)

#Main
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')



drawRandomCircle()

# canvas.bind("<Button-1>", drawRandomCircle)

# call the draw cicle after 5 seconds
root.mainloop()