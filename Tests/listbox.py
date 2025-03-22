from tkinter import *
from tkinter.ttk import *

janela=Tk()

lista=Listbox(janela, height=5)
lista.grid(column=0, row=0)
def fazer():
    print(lista.get(ACTIVE))
def fazer2():
    lista.delete(ANCHOR)
lista.insert(0, 'bem legal')
lista.insert(1, 'legal')
lista.insert(2, 'mais ou menos')
lista.insert(3, 'chato')
lista.insert(4, 'muito chato')
b1=Button(janela, text='apagar', command=fazer2)
b1.grid(column=1, row=1)
b=Button(janela, text='aperte paa saber', command=fazer)
b.grid(column=0, row=1)

#saber posição
def clique(retorno):
    print(f'x:{retorno.x} / y : {retorno.y} geo :{janela.geometry()}')
janela.bind('<Button-3>', clique)
janela.mainloop()