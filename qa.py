from Tkinter import *

root = Tk()

gameFrame = Frame(root)
gameFrame.pack()

button1 = Button(gameFrame)
button1["text"] = "Roll"
button1["background"] = "green"
button1.pack

root.mainloop()