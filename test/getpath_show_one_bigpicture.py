from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
root=Tk()

def xz():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename =""
        for i in range(0,len(filenames)):
            string_filename += str(filenames[i])
        lb.config(text = "您选择的文件是："+string_filename)
        return string_filename
    else:
        lb.config(text = "您没有选择任何文件");
lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="弹出选择文件对话框",command=xz)
def B():
    dd=xz()
    print (dd)
    word='beautiful'
    textLabel=Label(root,text=word)
    textLabel.pack()
    im=Image.open(dd)
    tkimg=ImageTk.PhotoImage(im)
    imgLabel=Label(root,imag=tkimg)
    imgLabel.pack()
    mainloop()
B()
