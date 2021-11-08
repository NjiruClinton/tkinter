""" Importing libraries. """
import tkinter
from tkinter import *
from tkinter import messagebox

# Assigning values to variables.
val = ""
A = 0
operator = ""

# Creating root window.
root = tkinter.Tk()
# Setting geometry.
root.geometry("250x400+300+300")
# Disabeling rezize option.
root.resizable(0, 0)
root.title("Task 9.1.x")

""" Class BtnClick to keep code clean. """


class BtnClick:
    global btn1_clicked

    def btn1_clicked():
        global val
        # Adding string value '1' to val variable.
        val = val + "1"
        data.set(val)

    global btn2_clicked

    def btn2_clicked():
        global val
        # Adding string value '2' to val variable.
        val = val + "2"
        data.set(val)

    global btn3_clicked

    def btn3_clicked():
        global val
        # Adding string value '3' to val variable.
        val = val + "3"
        data.set(val)

    global btn4_clicked

    def btn4_clicked():
        global val
        # Adding string value '4' to val variable.
        val = val + "4"
        data.set(val)

    global btn5_clicked

    def btn5_clicked():
        global val
        # Adding string value '5' to val variable.
        val = val + "5"
        data.set(val)

    global btn6_clicked

    def btn6_clicked():
        global val
        # Adding string value '6' to val variable.
        val = val + "6"
        data.set(val)

    global btn7_clicked

    def btn7_clicked():
        global val
        # Adding string value '7' to val variable.
        val = val + "7"
        data.set(val)

    global btn8_clicked

    def btn8_clicked():
        global val
        # Adding string value '8' to val variable.
        val = val + "8"
        data.set(val)

    global btn9_clicked

    def btn9_clicked():
        global val
        # Adding string value '9' to val variable.
        val = val + "9"
        data.set(val)

    global btn0_clicked

    def btn0_clicked():
        global val
        # Adding string value '0' to val variable.
        val = val + "0"
        data.set(val)

    global btn_add_clicked

    def btn_add_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "+"
        val = val + "+"
        data.set(val)

    global btn_sub_clicked

    def btn_sub_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "-"
        val = val + "-"
        data.set(val)

    global btn_mul_clicked

    def btn_mul_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "*"
        val = val + "*"
        data.set(val)

    global btn_div_clicked

    def btn_div_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "/"
        val = val + "/"
        data.set(val)

    global btn_equal_clicked

    def btn_equal_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "="
        val = val + "="
        data.set(val)

    global btn_clear_clicked

    def btn_clear_clicked():
        global A
        global operator
        global val
        val = ""
        A = 0
        operator = ""
        data.set(val)

    global result

    def result():
        global A
        global operator
        global val
        val2 = val
        if operator == "+":
            x = int((val2.split("+")[1]))
            c = A + x
            data.set(c)
            val = str(c)

        elif operator == "-":
            x = int((val2.split("-")[1]))
            c = A - x
            data.set(c)
            val = str(c)

        elif operator == "*":
            x = int((val2.split("*")[1]))
            c = A * x
            data.set(c)
            val = str(c)

        elif operator == "/":
            x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.show("Error!")
            A == ""
            val = ""
            data.set(val)

        else:
            c = int(A / x)
            data.set(c)
            val = str(c)


data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    textvariable=data,
    background="#ffffff",
    fg="#000000"
)
lbl.pack(expand=True, fill="both", )

# Frame Coding for Buttons
# Frame for root window
# Frame 1
btnrow1 = Frame(root, bg="#000000")
# If frame gets some space it can expand
btnrow1.pack(expand=True, fill="both", )

# Frame 2
btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both", )

# Frame 3
btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both", )

# Frame 4
btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both", )

""" Button row one. """
# Button 7
btn7 = Button(
    btnrow1,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn7_clicked,
)
# Buttons side by side
btn7.pack(side=LEFT, expand=True, fill="both", )

# Button 8
btn8 = Button(
    btnrow1,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn8_clicked,
)
# Buttons side by side
btn8.pack(side=LEFT, expand=True, fill="both", )

# Button 9
btn9 = Button(
    btnrow1,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn9_clicked,
)
# Buttons side by side
btn9.pack(side=LEFT, expand=True, fill="both", )

# Button Add
btnadd = Button(
    btnrow1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_add_clicked,
)
# Buttons side by side
btnadd.pack(side=LEFT, expand=True, fill="both", )

""" Button row two. """
# Button 4
btn4 = Button(
    btnrow2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn4_clicked,
)
# Buttons side by side
btn4.pack(side=LEFT, expand=True, fill="both", )

# Button 5
btn5 = Button(
    btnrow2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn5_clicked,
)
# Buttons side by side
btn5.pack(side=LEFT, expand=True, fill="both", )

# Button 4
btn6 = Button(
    btnrow2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn6_clicked,
)
# Buttons side by side
btn6.pack(side=LEFT, expand=True, fill="both", )

# Button Substract
btnsub = Button(
    btnrow2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_sub_clicked,
)
# Buttons side by side
btnsub.pack(side=LEFT, expand=True, fill="both", )

""" Button row three. """
# Button 1
btn1 = Button(
    btnrow3,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn1_clicked,
)
# Buttons side by side
btn1.pack(side=LEFT, expand=True, fill="both", )

# Button 2
btn2 = Button(
    btnrow3,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn2_clicked,
)
# Buttons side by side
btn2.pack(side=LEFT, expand=True, fill="both", )

# Button 3
btn3 = Button(
    btnrow3,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn3_clicked,
)
# Buttons side by side
btn3.pack(side=LEFT, expand=True, fill="both", )

# Button Multiply
btnmul = Button(
    btnrow3,
    text="*",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_mul_clicked,
)
# Buttons side by side
btnmul.pack(side=LEFT, expand=True, fill="both", )

""" Button row four. """
# Button 0
btn0 = Button(
    btnrow4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn0_clicked,
)
# Buttons side by side
btn0.pack(side=LEFT, expand=True, fill="both", )

# Button Clear
btnclr = Button(
    btnrow4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_clear_clicked,
)
# Buttons side by side
btnclr.pack(side=LEFT, expand=True, fill="both", )

# Button Equal to
btneq = Button(
    btnrow4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_equal_clicked,
)
# Buttons side by side
btneq.pack(side=LEFT, expand=True, fill="both", )

# Button Divide
btndiv = Button(
    btnrow4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked,
)
# Buttons side by side
btndiv.pack(side=LEFT, expand=True, fill="both", )

root.mainloop()


