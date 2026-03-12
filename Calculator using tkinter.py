from tkinter import *

# Create main window
root = Tk()
root.title("Calculator")
root.geometry("300x380")

# Entry field
entry = Entry(root, width=20, borderwidth=5, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to insert numbers
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

# Clear function
def clear():
    entry.delete(0, END)

# Operation functions
def add():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = "add"
    entry.delete(0, END)

def subtract():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = "sub"
    entry.delete(0, END)

def multiply():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = "mul"
    entry.delete(0, END)

def divide():
    global f_num
    global operation
    f_num = float(entry.get())
    operation = "div"
    entry.delete(0, END)

# Equal function
def equal():
    second_num = float(entry.get())
    entry.delete(0, END)

    if operation == "add":
        entry.insert(0, f_num + second_num)
    elif operation == "sub":
        entry.insert(0, f_num - second_num)
    elif operation == "mul":
        entry.insert(0, f_num * second_num)
    elif operation == "div":
        entry.insert(0, f_num / second_num)

# Buttons
btn1 = Button(root, text="1", padx=20, pady=20, command=lambda: click(1))
btn2 = Button(root, text="2", padx=20, pady=20, command=lambda: click(2))
btn3 = Button(root, text="3", padx=20, pady=20, command=lambda: click(3))
btn4 = Button(root, text="4", padx=20, pady=20, command=lambda: click(4))
btn5 = Button(root, text="5", padx=20, pady=20, command=lambda: click(5))
btn6 = Button(root, text="6", padx=20, pady=20, command=lambda: click(6))
btn7 = Button(root, text="7", padx=20, pady=20, command=lambda: click(7))
btn8 = Button(root, text="8", padx=20, pady=20, command=lambda: click(8))
btn9 = Button(root, text="9", padx=20, pady=20, command=lambda: click(9))
btn0 = Button(root, text="0", padx=20, pady=20, command=lambda: click(0))

btn_add = Button(root, text="+", padx=20, pady=20, command=add)
btn_sub = Button(root, text="-", padx=20, pady=20, command=subtract)
btn_mul = Button(root, text="*", padx=20, pady=20, command=multiply)
btn_div = Button(root, text="/", padx=20, pady=20, command=divide)
btn_eq = Button(root, text="=", padx=20, pady=20, command=equal)
btn_clr = Button(root, text="C", padx=20, pady=20, command=clear)

# Button layout
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)

btn_add.grid(row=1, column=3)
btn_sub.grid(row=2, column=3)
btn_mul.grid(row=3, column=3)
btn_div.grid(row=4, column=3)

btn_eq.grid(row=4, column=2)
btn_clr.grid(row=4, column=1)

root.mainloop()