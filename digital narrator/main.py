from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Text to speech")
root.geometry("400x330")
root.resizable(FALSE, FALSE)
root.iconbitmap("icon.ico")
background_img = ImageTk.PhotoImage(Image.open('bg.jpeg'))
bgimage = Label(root, image=background_img).place(x=0, y=0, relwidth=1)


def process():
    pass


def cancel():
    root.quit()


label1 = Label(root, text='Select the text file below:',  fg='white', font=('Garamond', 15)).place(x=30, y=30)
label2 = Label(root, text='Write the name of the audio file below:', fg='white', font=('Garamond', 15)).place(x=30, y=180)

button1 = Button(root, text='Process', fg='black', bg='#000fff', command=process).place(x=50, y=280, width=100, height=30)
button2 = Button(root, text='Cancel', fg='black', bg='#000fff', command=cancel).place(x=250, y=280, width=100, height=30)



root.mainloop()