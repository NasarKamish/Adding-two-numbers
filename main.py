from tkinter import *

Addition = Tk()
Addition.title("Adding two numbers")


def add():
    my_sum = str(float(en_First.get()) + float(en_Second.get()))
    addition.set(my_sum)


def clear():
    en_First.delete(0, END)
    en_Second.delete(0, END)


addition = StringVar()
Addition.geometry("380x130")
lbl_First = Label(Addition, text="Please enter first number: ")
lbl_First.place(x=0, y=0)
en_First = Entry(Addition)
en_First.place(x=210, y=0)
lbl_Second = Label(Addition, text="Please enter second number: ")
lbl_Second.place(x=0, y=30)
en_Second = Entry(Addition)
en_Second.place(x=210, y=30)
lbl_Answer = Label(Addition, text="Your answer: ")
lbl_Answer.place(x=0, y=60)
lbl_Answer2 = Label(Addition, textvariable=addition)
lbl_Answer2.place(x=210, y=60)
btn_Add = Button(Addition, text="Add", command=add)
btn_Clear = Button(Addition, text="Clear", command=clear)
btn_Exit = Button(Addition, text="Exit", command=exit)
btn_Add.place(x=0, y=90)
btn_Clear.place(x=60, y=90)
btn_Exit.place(x=130, y=90)
Addition.mainloop()
