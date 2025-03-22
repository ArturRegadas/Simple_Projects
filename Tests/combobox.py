from tkinter import *
from tkinter.ttk import *

janela=Tk()
janela.title('opções')
combo = Combobox(janela)
combo['values']=('o', 'ol', 'ola', 'ola m', 'ola me')
combo.current(0)
combo.grid(column=0, row=0)
c=combo.get()
msg=Label(janela, text=c)
msg.grid(column=0, row=1)
janela.mainloop()