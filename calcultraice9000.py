from tkinter import *

# global layout
root = Tk()
root.geometry("258x470")
root.title("calculatrice9000")
expression = ""
equation = StringVar()
expression_field = Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=17, ipady=12)

# oparator label

# number label and layout
def label_num():
    i = 1
    btns = []
    for j in range(3, 6):
        for k in range(3):
            btns.append(Button(command=lambda i=i: button_click(i), text=i, height=3, width=5, font=14).grid(row=[j], column=[k]))
            i += 1

    Button(command=lambda: button_click(0), text="0", height=3, width=5, font=10).grid(row=6, column=1)

label_num()


#operator layout
label_equal = Button(text="=", width=5, height=3, font=10, bg="dark orange", command=lambda: button_equal())
label_plus = Button(text="+", width=5, height=3, font=10, bg="dark orange", command=lambda: button_click("+"))
label_minus = Button(text="-", width=5, height=3, font=10, bg="gray44", command=lambda: button_click("-"))
label_divide = Button(text="/", width=5, height=3, font=10, bg="grey44", command=lambda: button_click("/"))
label_multiply = Button(text="x", width=5, height=3, font=10, bg="dark orange", command=lambda: button_click("*"))
label_clear = Button(text="C", width=5, height=3, font=10, bg="gray68", command=lambda: button_clear())
label_dot = Button(text=".", width=5, height=3, font=10, bg="gray68", command=lambda: button_click("."))
label_square = Button(text="sqr", width=5, height=3, font=10, bg="grey44", command=lambda: button_square())
label_percentage = Button(text="%", width=5, height=3, font=10, bg="dark orange", command=lambda: button_click("//"))
label_squareroot = Button(text="sqrt", width=5, height=3, font=10, bg="dark orange", command=lambda: button_squareroot())
root.bind(1, lambda event: button_click(1))
root.bind(2, lambda event: button_click(2))
root.bind(3, lambda event: button_click(3))
root.bind(4, lambda event: button_click(4))
root.bind(5, lambda event: button_click(5))
root.bind(6, lambda event: button_click(6))
root.bind(7, lambda event: button_click(7))
root.bind(8, lambda event: button_click(8))
root.bind(9, lambda event: button_click(9))
root.bind(0, lambda event: button_click(0))



#button fonction
def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def button_equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("Error")
        expression = ""


# oparot layout
label_equal.grid(row=6, column=3)
label_plus.grid(row=3, column=3)
label_percentage.grid(row=4, column=3)
label_multiply.grid(row=5, column=3)
label_clear.grid(row=6, column=0)
label_dot.grid(row=6, column=2)
label_divide.grid(row=2, column=0)
label_minus.grid(row=2, column=1)
label_square.grid(row=2, column=2)
label_squareroot.grid(row=2, column=3)

# Button for the "sqrt" operator
def button_squareroot():
    global expression
    expression = str(float(equation.get())**0.5)
    equation.set(expression)

# Button for the 2 operator
def button_square():
    global expression
    expression = str(float(equation.get())**2)
    equation.set(expression)


def button_clear():
    global expression
    expression = ""
    equation.set("")




root.mainloop()