from tkinter import *
# created a function to clear the text area
def clear_screen():
    display.set("")
# function to insert values into the text area
def data_insertion(value):
    if display.get()=="ERROR":
        clear_screen()
    word=display.get()+value
    display.set(word)
window=Tk()
window.geometry("730x355")
display=StringVar()
display_text=Entry(window, width=46, bd=20, textvariable=display,justify="right",bg="Gray")
display_text.grid(row=0,column=0,columnspan=4)

window.mainloop()