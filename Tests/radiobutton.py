from tkinter import *
from tkinter.ttk import *

janela=Tk()

radio=Radiobutton(janela, text='sim', value=0)
radio.grid(column=0, row=0)
radio1=Radiobutton(janela, text='não', value=1)
radio1.grid(column=1, row=0)


janela.mainloop()