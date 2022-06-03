from tkinter import*
CALC=Tk()
def entrada(valor):
            lb1['text'] += valor

def saida():

    resultado = eval(lb1['text'])
    lb1['text'] = str(resultado)

def limpar():
    lb1['text'] = ''




lb1 = Label()
lb2 = Button (CALC, text= "7", font= 'Arial 26', command=lambda: entrada('7'))
lb3 = Button (CALC, text= "8", font= 'Arial 26', command=lambda: entrada('8'))
lb4 = Button (CALC, text= "9", font= 'Arial 26', command=lambda: entrada('9'))
lb5 = Button (CALC, text= "*", font= 'Arial 26', command=lambda: entrada('*'))
lb6 = Button (CALC, text= "4", font= 'Arial 26', command=lambda: entrada('4'))
lb7 = Button (CALC, text= "5", font= 'Arial 26', command=lambda: entrada('5'))
lb8 = Button (CALC, text= "6", font= 'Arial 26', command=lambda: entrada('6'))
lb9 = Button (CALC, text= "/", font= 'Arial 26', command=lambda: entrada('/'))
lb10 = Button (CALC, text= "1", font= 'Arial 26', command=lambda: entrada('1'))
lb11 = Button (CALC, text= "2", font= 'Arial 26', command=lambda: entrada('2'))
lb12 = Button (CALC, text= "3", font= 'Arial 26', command=lambda: entrada('3'))
lb13 = Button (CALC, text= "+", font= 'Arial 26', command=lambda: entrada('+'))
lb14 = Button (CALC, text= "0", font= 'Arial 26', command=lambda: entrada('0'))
lb15 = Button (CALC, text= "=", font= 'Arial 26', command=lambda: saida())
lb16 = Button (CALC, text= ".", font= 'Arial 26', command=lambda: entrada('.'))
lb17 = Button (CALC, text= "-", font= 'Arial 26', command=lambda: entrada('-'))
lb18 = Button (CALC, text= "Del", font= 'Arial 26', command=lambda: limpar())
lb19 = Button (CALC, text= "C", font= 'Arial 26', command=lambda: entrada('C'))
lb20 = Button (CALC, text= "(", font= 'Arial 26', command=lambda: entrada('('))
lb21 = Button (CALC, text= ")", font= 'Arial 26', command=lambda: entrada(')'))

lb1.grid(row=0, column=0, sticky=NSEW)
lb2.grid(row=1, column=0, sticky=NSEW)
lb3.grid(row=1, column=1, sticky=NSEW)
lb4.grid(row=1, column=2, sticky=NSEW)
lb5.grid(row=1, column=3, sticky=NSEW)
lb6.grid(row=2, column=0, sticky=NSEW)
lb7.grid(row=2, column=1, sticky=NSEW)
lb8.grid(row=2, column=2, sticky=NSEW)
lb9.grid(row=2, column=3, sticky=NSEW)
lb10.grid(row=3, column=0, sticky=NSEW)
lb11.grid(row=3, column=1, sticky=NSEW)
lb12.grid(row=3, column=2, sticky=NSEW)
lb13.grid(row=3, column=3, sticky=NSEW)
lb14.grid(row=4, column=0, sticky=NSEW)
lb15.grid(row=4, column=1, sticky=NSEW)
lb16.grid(row=4, column=2, sticky=NSEW)
lb17.grid(row=4, column=3, sticky=NSEW)
lb18.grid(row=5, column=0, sticky=NSEW)
lb19.grid(row=5, column=1, sticky=NSEW)
lb20.grid(row=5, column=2, sticky=NSEW)
lb21.grid(row=5, column=3, sticky=NSEW)

lb1.grid(row=0,column=0, sticky=NSEW)
CALC.grid_rowconfigure(0,weight=1)
CALC.grid_rowconfigure(1,weight=1)
CALC.grid_rowconfigure(2,weight=1)
CALC.grid_rowconfigure(3,weight=1)
CALC.grid_rowconfigure(4,weight=1)
CALC.grid_rowconfigure(5,weight=1)
CALC.grid_columnconfigure(0,weight=1)
CALC.grid_columnconfigure(1,weight=1)
CALC.grid_columnconfigure(2,weight=1)
CALC.grid_columnconfigure(3,weight=1)

mainloop()