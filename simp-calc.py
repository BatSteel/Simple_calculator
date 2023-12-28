from tkinter import *

window=Tk()
window.geometry("730x355")
display=StringVar()
display_text=Entry(window, width=46, bd=20, textvariable=display,justify="right",bg="Gray")
display_text.grid(row=0,column=0,columnspan=4)

window.mainloop()