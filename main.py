from tkinter import *

Addition = Tk()
Addition.title("Adding two numbers")


def add():
    my_sum = str(int(en_First.get()) + int(en_Second.get()))
    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.insert(0, my_sum)
    en_Answer.config(state="readonly")
    addition.set(my_sum)


def clear():
    en_First.delete(0, END)
    en_Second.delete(0, END)
    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")


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
en_Answer = Entry(Addition)
en_Answer.config(state="readonly")
en_Answer.place(x=210, y=60)
btn_Add = Button(Addition, text="Add", command=add)
btn_Clear = Button(Addition, text="Clear", command=clear)
btn_Exit = Button(Addition, text="Exit", command=exit)
btn_Add.place(x=0, y=90)
btn_Clear.place(x=60, y=90)
btn_Exit.place(x=130, y=90)
Addition.mainloop()
