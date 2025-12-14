from tkinter import*
window=Tk()
window.title=("calculator")
window.geometry("500x500")
def set_number(num):
    equation.set(equation.get()+num)
def cal():
    equation.set(eval(equation.get()))
def backspace():
    current=equation.get()
    equation.set(current[:-1])
def sign(s):
    x=equation.get()[-1]
    if x=="+" or x=="-" or x=="*" or x=="/":
        equation.set(equation.get()[:-1]+s)
    else:
        equation.set(equation.get()+s)
def press_power():
    equation.set(equation.get()+"**")
def press_percent():
    equation.set(equation.get()+"/100")
def press_sqrt():
    equation.set(equation.get()+"**0.5")
def plus_minus():
    if equation.get().startswith("-"):
        equation.set(equation.get()[1:])
    else:
        equation.set("-"+equation.get())
def paranthes():
    if equation.get()=="":
        equation.set("(")
        return
    if equation.get()[-1] in "+-*/(":
        equation.set(equation.get()+"(")
        return
    equation.__set(equation.get()+")")


equation=StringVar()
lbl1=Label(textvariable=equation,font=("times new roman",12,"bold"),padx=5,pady=10,fg="blue",bg="silver")
lbl1.grid(columnspan=4)
btn1=Button(text="1",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("1"))
btn1.grid(row=1,column=0)
btn2=Button(text="2",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("2"))
btn2.grid(row=1,column=1)
btn3=Button(text="3",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("3"))
btn3.grid(row=1,column=2)
btn4=Button(text="4",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("4"))
btn4.grid(row=2,column=0)
btn5=Button(text="5",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("5"))
btn5.grid(row=2,column=1)
btn6=Button(text="6",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("6"))
btn6.grid(row=2,column=2)
btn7=Button(text="7",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("7"))
btn7.grid(row=3,column=0)
btn8=Button(text="8",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("8"))
btn8.grid(row=3,column=1)
btn9=Button(text="9",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("9"))
btn9.grid(row=3,column=2)
btn0=Button(text="0",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:set_number("0"))
btn0.grid(row=4,column=1)
btnmul=Button(text="*",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:sign("*"))
btnmul.grid(row=1,column=3)
btndive=Button(text="/",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:sign("/"))
btndive.grid(row=2,column=3)
btnplus=Button(text="+",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:sign("+"))
btnplus.grid(row=3,column=3)
btnsub=Button(text="-",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:sign("-"))
btnsub.grid(row=4,column=3)
btnc=Button(text="c",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=backspace)
btnc.grid(row=4,column=0)
btne=Button(text="=",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=cal)
btne.grid(row=4,column=2)
btnpercent=Button(text="%",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:press_percent())
btnpercent.grid(row=5,column=0)
btnpow=Button(text="^",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:press_power())
btnpow.grid(row=5,column=1)
btnsquare_root=Button(text="sqrt",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:press_sqrt())
btnsquare_root.grid(row=5,column=2)
btnplus_minus=Button(text="+/-",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:plus_minus())
btnplus_minus.grid(row=5,column=3)
btnpranthes=Button(text="(",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:paranthes())
btnpranthes.grid(row=1,column=4)
btnpranthes=Button(text=")",font=("times new roman",12,"bold"),fg="#0AB2F5",bg="#AB9A96",width=5,height=2,command=lambda:paranthes())
btnpranthes.grid(row=2,column=4)
window.mainloop()
