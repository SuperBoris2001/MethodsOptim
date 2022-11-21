import tkinter
from tkinter import *
from sympy import poly, Symbol
import math
# импортировали библиотеки
def GoldenRatioFunction(Func,a,b,eps):
    F = 1.6180339887498948482 # пропорция золотого сечения
    while(abs(b-a)>=eps):
        E = (b-a)/F
        x1 = b - E
        x2 = a + E
        y1 = Func(x1)
        y2 = Func(x2)
        if (y1 >= y2): # для поиска минимума, для поиска максимума y1 <= y2
            a = x1
        else:
            b = x2
    x = (b + a)/2
    return Func(x)
def get_entry():
    eps = 0.0001
    # try:
    #
    # except:
    #  print('Неверный ввод!')
    value = str(edit.get())
    if value:
        value = value.replace('^','**')
        y = poly(value) # преобразовали строку в полином
        a_ = float(edita.get())
        b_ = float(editb.get())

        if ((a_ == '') | (b_ == '') ):
         print('Empty a или b !')
        elif (a_ > b_):
         print(' a больше b !')
        else:
            res = GoldenRatioFunction(y,a_,b_,eps)
            print(res)

    else:
        print('Empty!')
# функция ввода полинома
win = Tk()
win.geometry('600x200+200+200')
win.title('Методы оптимизации')
win.resizable(False,False)
photo = PhotoImage(file = 'my_fun_icon.png')
win.iconphoto(False, photo)
t1 = Label(win, text = 'Enter your polinom!', fg = 'blue').grid(row = 0, column = 0, stick= 'w')
#t1.config(font= ('Verdana', 25))
#t1.pack()
edit = Entry(win, bg = 'violet')
edit.grid(row = 0, column = 1)
edita = Entry(win, bg = 'violet')
edita.grid(row = 0, column = 2)
editb = Entry(win, bg = 'violet')
editb.grid(row = 0, column = 3)
but = Button(win, text = 'Click my', command=get_entry).grid(row = 1, column=0,stick = 'we')
#edit.pack()
win.columnconfigure(0, minsize=200)
win.columnconfigure(1, minsize=100)
win.mainloop()


