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
    canvas.move("go", -20,0)
    # canvas.after(700, go)

def drawRandomCircle():
    global X,Y
    y1 = random.randrange(350,600)
    y2 = random.randrange(100,280)
    color = random.choice(colors)
    canvas.create_rectangle(500+X, 0, 550+X, y2, fill=color, tags="go")
    canvas.create_rectangle(500+X, y1, 550+X, 600, fill=color, tags="go")
    X += 130
    canvas.after(100, drawRandomCircle)
    go()

def click():
    canvas.move("sharp", 0,5)
    canvas.after(100, click)

def moveup(event):
    canvas.move("sharp", 0,-30)


def onClick():
    canvas.delete("button")
    #Create sharp
    canvas.create_oval(200, 200, 250, 250, fill=random.choice(colors), tags="sharp")
    canvas.bind("<Button-1>", moveup)
    drawRandomCircle()
    click()

#Main
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')


# create a button
button = tk.Button(root, text="Start", command=onClick)
button.pack()


# call the draw cicle after 5 seconds
root.mainloop()