import Tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
s='1cp1.jpeg'
im=Image.open(s)
tkimg=ImageTk.PhotoImage(im)
l=tk.Label(root,image=tkimg)
l.pack()
root.mainloop()
