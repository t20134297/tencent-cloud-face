from tkinter import *
from PIL import Image, ImageTk
import sys
path1 = sys.argv[1]
def A():
    root=Tk()#注意Tk的大小写
    textLabel=Label(root,text='舍名利')
    textLabel.pack()
    # s='/home/ansheng/Desktop/face_detect/test/1cp1.jpeg'
    im=Image.open(path1)
    tkimg=ImageTk.PhotoImage(im)
    imgLabel=Label(root,imag=tkimg)
    imgLabel.pack()
    mainloop()
A()
