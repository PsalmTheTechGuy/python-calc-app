from tkinter import *
root = Tk()
root.iconbitmap('c:\GUI\logo.ico')
root.title('Calculator')
# root.resizable(False, False)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)


# responsible for inserting to the entry widget
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    


# This functions clears data    
def clear_click():
    e.delete(0, END)
    
def plus_click():
    global first_num
    global math
    math = 'addition'
    first_num = e.get()
    e.delete(0, END)
    
def multiply_click():
    global first_num
    global math
    math = 'multiplication'
    first_num = e.get()
    e.delete(0, END)
    
def subtract_click():
    global first_num
    global math
    math = 'subtraction'
    first_num = e.get()
    e.delete(0, END)
    
def divide_click():
    global first_num
    global math
    math = 'division'
    first_num = e.get()
    e.delete(0, END)
    

    
def equal_click():
    second_num = e.get()
    e.delete(0, END)
    if math == 'addition':
        result = int(first_num) + int(second_num)
    if math == 'multiplication':
        result = int(first_num) * int(second_num)
    if math == 'subtraction':
        result = int(first_num) - int(second_num)
    if math == 'division':
        result = int(first_num) / int(second_num)
    e.insert(0, result)
    
    
    
# def button_add(number):
#     current_num = e.get()
#     e.delete(0, END)
#     e.insert(0, current_num + number)




btn1 = Button(root, text=1, padx=40, pady=20, command = lambda: button_click(1))
btn2 = Button(root, text=2, padx=40, pady=20, command = lambda: button_click(2))
btn3 = Button(root, text=3, padx=40, pady=20, command = lambda: button_click(3))
btn4 = Button(root, text=4, padx=40, pady=20, command = lambda: button_click(4))
btn5 = Button(root, text=5, padx=40, pady=20, command = lambda: button_click(5))
btn6 = Button(root, text=6, padx=40, pady=20, command = lambda: button_click(6))
btn7 = Button(root, text=7, padx=40, pady=20, command = lambda: button_click(7))
btn8 = Button(root, text=8, padx=40, pady=20, command = lambda: button_click(8))
btn9 = Button(root, text=9, padx=40, pady=20, command = lambda: button_click(9))
btn_0 = Button(root, text=0, padx=40, pady=20,command = lambda: button_click(0))
btn_clear = Button(root, text='clear', padx=79, pady=20, command=clear_click)
btn9_eqaul = Button(root, text='=', padx=88, pady=20, command=equal_click)
btn_plus = Button(root, text='+', padx=40, pady=20, command=plus_click)
btn_multiply = Button(root, text='x', padx=40, pady=20, command=multiply_click)
btn_subtract = Button(root, text='-', padx=40, pady=20, command=subtract_click)
btn_divide = Button(root, text='/', padx=40, pady=20, command=divide_click)


btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn9_eqaul.grid(row=5, column=1, columnspan=2)
btn_plus.grid(row=5, column=0)
btn_multiply.grid(row=6, column=0)
btn_subtract.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)

root.mainloop() 