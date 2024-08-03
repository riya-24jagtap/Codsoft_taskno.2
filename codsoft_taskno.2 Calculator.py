from tkinter import*
win = Tk()
win.geometry("350x480")
win.title("Calculator")
winlabel = Label(win,text=" ", bg='dark gray',font=("Times",25,'bold'))
winlabel.pack(side=TOP)
win.config(background='dark gray')

# Initialize a StringVar for text input 
textin=StringVar()
expression=" "


#number input
def click_but(number):
    global expression
    expression = expression + str(number)
    textin.set(expression)
    
#calculates the expression
def equal_but():
    global expression
    result=str(eval(expression))
    textin.set(result)
    expression=''

#clearing button   
def clear_but():
    global expression
    expression = ''
    textin.set('')
    
#input field
input_text = Entry(win,font=("arial",12,'bold'), textvar=textin, width=100, bd=5, bg='white')
input_text.pack()

#numbers
one=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(1),text="1",font=("Stencil Std",16,'bold'))
one.place(x=10,y=100)

two=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(2),text="2",font=("Stencil Std",16,'bold'))
two.place(x=10,y=170)

three=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(3),text="3",font=("Stencil Std",16,'bold'))
three.place(x=10,y=240)

four=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(4),text="4",font=("Stencil Std",16,'bold'))
four.place(x=75,y=100)

five=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(5),text="5",font=("Stencil Std",16,'bold'))
five.place(x=75,y=170)

six=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(6),text="6",font=("Stencil Std",16,'bold'))
six.place(x=75,y=240)

seven=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(7),text="7",font=("Stencil Std",16,'bold'))
seven.place(x=140,y=100)

eight=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(8),text="8",font=("Stencil Std",16,'bold'))
eight.place(x=140,y=170)

nine=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(9),text="9",font=("Stencil Std",16,'bold'))
nine.place(x=140,y=240)

zero=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:click_but(0),text="0",font=("Stencil Std",16,'bold'))
zero.place(x=10,y=310)

#Operation buttons
add=Button(win,padx=12,pady=14,bd=4,bg='white',text="+",command=lambda:click_but("+"),font=("Stencil Std",16,'bold'))
add.place(x=205,y=100)

subt=Button(win,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:click_but("-"),font=("Stencil Std",16,'bold'))
subt.place(x=205,y=170)

mult=Button(win,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:click_but("*"),font=("Stencil Std",16,'bold'))
mult.place(x=205,y=240)

div=Button(win,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:click_but("/"),font=("Stencil Std",16,'bold'))
div.place(x=205,y=310)

dot=Button(win,padx=47,pady=13,bd=4,bg='white',command=lambda:click_but("."),text=".",font=("Stencil Std",16,'bold'))
dot.place(x=75,y=310)

equal=Button(win,padx=151,pady=14,bd=4,bg='white',command=equal_but,text="=",font=("Stencil Std",16,'bold'))
equal.place(x=10,y=380)

clear=Button(win,padx=14,pady=110,bd=4,bg='white',text="C",command=clear_but,font=("Stencil Std",16,'bold'))
clear.place(x=270,y=100)




win.mainloop()