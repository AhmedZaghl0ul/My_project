from tkinter import *   
gui = Tk()
gui.title("simple calculator")
gui.geometry("280x250")
gui.title("Calculator App")
titlelabel =Label(gui , text=("Calculator App") , fg=("black") ,
 font=("Century 20 bold"))
titlelabel.grid(columnspan=4)

expression = ""

def press(num):
	global expression

	expression = expression + str(num)
	equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("input error")
        expression = ""

def clear():
     global expression
     expression = ""
     equation.set("")

equation = StringVar()
expresstionf= Entry(gui,textvariable=equation)
expresstionf.grid(columnspan=4 , ipadx=80)

but1 = Button(gui, text=' 1 ', fg='white', 
bg='black',command=lambda: press(1), height=1, width=7)
but1.grid(row=2, column=0)

but2 = Button(gui, text=' 2 ',fg='white', 
bg='black',command=lambda: press(2), height=1, width=7)
but2.grid(row=2, column=1)

but3 = Button(gui, text=' 3 ', fg='white', 
bg='black',command=lambda: press(3), height=1, width=7)
but3.grid(row=2, column=2)

but4 = Button(gui, text=' 4 ', fg='white',
 bg='black',command=lambda: press(4), height=1, width=7)
but4.grid(row=3, column=0)

but5 = Button(gui, text=' 5 ', fg='white',
 bg='black',command=lambda: press(5), height=1, width=7)
but5.grid(row=3, column=1)

but6 = Button(gui, text=' 6 ', fg='white', 
bg='black',command=lambda: press(6), height=1, width=7)
but6.grid(row=3, column=2)

but7 = Button(gui, text=' 7 ', fg='white', 
bg='black',command=lambda: press(7), height=1, width=7)
but7.grid(row=4, column=0)

but8 = Button(gui, text=' 8 ',fg='white', 
bg='black',command=lambda: press(8), height=1, width=7)
but8.grid(row=4, column=1)

but9 = Button(gui, text=' 9 ', fg='white',
 bg='black',command=lambda: press(9), height=1, width=7)
but9.grid(row=4, column=2)

but0 = Button(gui, text=' 0 ', fg='white', 
bg='black',command=lambda: press(0), height=1, width=7)
but0.grid(row=5, column=0)

plus = Button(gui, text=' + ', fg='white', 
bg='green',command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', fg='white', 
bg='green',command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(gui, text=' * ', fg='white' , 
bg='green',command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(gui, text=' / ', fg='white',
bg='green',command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(gui, text=' = ', fg='white', 
bg='red',command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', fg='white', 
bg='red',command=clear, height=1, width=7)
clear.grid(row=5, column='1')

dotbutt= Button(gui, text='.', fg='white', 
bg='black',command=lambda: press('.'), height=1, width=7)
dotbutt.grid(row=6, column=0)

gui.mainloop()
