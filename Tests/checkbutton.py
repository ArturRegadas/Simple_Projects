from tkinter import *
from tkinter.ttk import *
janela=Tk()
estado=IntVar()
check=Checkbutton(janela, text='usara login anonimo', var=estado, onvalue=1, offvalue=0)

check.grid(column=0, row=0)
estado.set(0)
c=estado.get()



janela.mainloop()