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
display_text=Entry(window, width=33, bd=20, textvariable=display,justify="right",bg="Gray")
display_text.grid(row=1,column=1,columnspan=4)
# created 7,8,9 and clear button
b7=Button(window,text="7",bg="black",fg="red",command=lambda:data_insertion("7"),width=6,bd=5).place(x=0,y=60)
b8=Button(window,text="8",bg="black",fg="red",command=lambda:data_insertion("8"),width=6,bd=5).place(x=60,y=60)
b9=Button(window,text="9",bg="black",fg="red",command=lambda:data_insertion("9"),width=6,bd=5).place(x=120,y=60)
clear=Button(window,text="c",bg="red",fg="black",command=lambda:clear_screen(),width=6,bd=5).place(x=180,y=60)

# created 4,5,6 and + button
b4=Button(window,text="4",bg="black",fg="red",command=lambda:data_insertion("4"),width=6,bd=5).place(x=0,y=94)
b5=Button(window,text="5",bg="black",fg="red",command=lambda:data_insertion("5"),width=6,bd=5).place(x=60,y=94)
b6=Button(window,text="6",bg="black",fg="red",command=lambda:data_insertion("6"),width=6,bd=5).place(x=120,y=94)
plus=Button(window,text="+",bg="black",fg="red",command=lambda:data_insertion("+"),width=6,bd=5).place(x=180,y=94)

window.mainloop()