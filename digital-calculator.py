import tkinter
from tkinter import*

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btncleardisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def btnOff():
    global operator
    operator = ""
    exit(cal)


cal = Tk()
cal.title("calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=30,insertwidth=4,
             bg="powder blue", justify='right').grid(columnspan=4)

btnAC     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Ac", command=btncleardisplay,     bg="light grey").grid(row=1,column=0)
btnCancle = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" C ",                             bg="light grey").grid(row=1,column=1)
btnOff    = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Off",command=btnOff,              bg="light grey").grid(row=1,column=2)
Mod       = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="%",  command=lambda:btnClick("%"),bg="light grey").grid(row=1,column=3)

btn7     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 7 ",command=lambda:btnClick(7),  bg="light grey").grid(row=2,column=0)
btn8     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 8 ",command=lambda:btnClick(8),  bg="light grey").grid(row=2,column=1)
btn9     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 9 ",command=lambda:btnClick(9),  bg="light grey").grid(row=2,column=2)
Division = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" / ",command=lambda:btnClick("/"),bg="light grey").grid(row=2,column=3)

btn4     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 4 ",command=lambda:btnClick(4),  bg="light grey").grid(row=3,column=0)
btn5     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 5 ",command=lambda:btnClick(5),  bg="light grey").grid(row=3,column=1)
btn6     = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 6 ",command=lambda:btnClick(6),  bg="light grey").grid(row=3,column=2)
Multiply = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" X ",command=lambda:btnClick("*"),bg="light grey").grid(row=3,column=3)

btn1         = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 1 ",command=lambda:btnClick(1),  bg="light grey").grid(row=4,column=0)
btn2         = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 2 ",command=lambda:btnClick(2),  bg="light grey").grid(row=4,column=1)
btn3         = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 3 ",command=lambda:btnClick(3),  bg="light grey").grid(row=4,column=2)
Substraction = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" - ",command=lambda:btnClick("-"),bg="light grey").grid(row=4,column=3)

btn0        = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" 0 ",command=lambda:btnClick(0),  bg="light grey").grid(row=5,column=0)
btnPoint    = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" . ",command=lambda:btnClick("."),bg="light grey").grid(row=5,column=1)
btnEqualsTo = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" = ",command=btnEqualsInput,      bg="light grey").grid(row=5,column=2)
Addition    = Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text=" + ",command=lambda:btnClick("+"),bg="light grey").grid(row=5,column=3)


cal.mainloop()