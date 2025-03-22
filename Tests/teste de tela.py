from tkinter import *

janela=Tk()
janela.title('somando numeros')

def clique(retorno):
    print(f'x:{retorno.x} / y : {retorno.y} geo :{janela.geometry()}')
janela.bind('<Button-3>', clique)

msg0=Label(janela, text='vamos fazer a soma de dois numeros')
msg0.grid(column=0, row=0)

msg1=Label(janela, text='digite o primeiro numero')
msg1.grid(column=0, row=1)

msg2=Label(janela, text='digite o segundo numero')
msg2.grid(column=0, row=2)

entrada=Entry(janela, width=10)
entrada.grid(column=1, row=1)

entrada1=Entry(janela, width=10)
entrada1.grid(column=1, row=2)



msg4=Label(janela, text='')
msg4.grid(column=1, row=4)

def soma():
    n = entrada.get()
    n=int(n)
    n1 = entrada1.get()
    n1=int(n1)
    z=n1+n
    msg4.configure(text=z)

msg5=Label(janela, text='a soma entre esses dois numeros é:')
msg5.grid(column=0, row=4)

msg3= Button (janela, text='obter resultado', command=soma)
msg3.grid(column=0, row=3)
janela.mainloop()