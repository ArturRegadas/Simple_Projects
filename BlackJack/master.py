from tkinter import *

janela=Tk()
janela.title("BlackJack 21")
janela.geometry("520x267")

with open("mymoney", "r") as arquivo:
	qtd = int(arquivo.read())

if qtd > 999 :
    serx=157
elif qtd < 100:
    serx=200
else:
    serx=180
labelframe=LabelFrame(janela, text="dinheiro", font="ProximaNova 25" )
labelframe.place(x=146, y=0, height=140, width=230)
dinheiro=Label(janela, text=qtd, font="ProximaNova 65")
dinheiro.place(x=serx, y=35)

with open("vitorias", "r") as arquivo1:
	historic = arquivo1.readlines()
lista=Listbox(janela)
lista.place(x=11,y=18)
lista.insert(0, historic[len(historic)-1])
lista.insert(1, historic[len(historic)-2])
lista.insert(2, historic[len(historic)-3])
lista.insert(3, historic[len(historic)-4])
lista.insert(4, historic[len(historic)-5])
lista.insert(5, historic[len(historic)-6])
lista.insert(6, historic[len(historic)-7])
lista.insert(7, historic[len(historic)-8])
lista.insert(8, historic[len(historic)-9])
lista.insert(9, historic[len(historic)-10])
def historico():
    x = 1
    janelahis=Tk()
    janelahis.title("Historico de Partidas")
    janelahis.geometry("320x720")
    historic2=[]
    for j in historic:
        historic2.append(historic[len(historic)-x])
        x=x+1

    labelhis=Label(janelahis, text=historic2)
    labelhis.place(x=0,y=0)
    janelahis.mainloop()
with open("vitorias", "r") as arquivov:
	ba = arquivov.read()
boyah=ba.count("Vitoria")
empate=ba.count("Empate")
derrota=ba.count("Derrota")
partidas=boyah+empate+derrota

labeljogos=Label(janela, text=f"Você jogou {partidas} vezes")
labeljogos.place(x=380, y=21)
labelvitorias=Label(janela, text=f"Você ganhou {boyah} vezes")
labelvitorias.place(x=380, y=51)
labelempates=Label(janela, text=f"Você empatou {empate} vezes")
labelempates.place(x=380, y=81)
labelderrotas=Label(janela, text=f"Você perdeu {derrota} vezes")
labelderrotas.place(x=380, y=111)
botahis=Button(janela, text="Historico", font="ProximaNova 15", command=historico)
botahis.place(x=11,y=185,height=30, width=124)
with open("fichas brancas", "r") as arquivob1:
    tab=arquivob1.read()

branco=Canvas(janela)
branco.place(x=140,y=145)
b=branco.create_oval(50, 50,5,5, fill="White")
b1=branco.create_text(27, 27, text=tab, font="ProximaNova 15")
with open("fichas Vermelhas", "r") as arquivov1:
    tav=arquivov1.read()

vermelho=Canvas(janela)
vermelho.place(x=228,y=145)
v=vermelho.create_oval(50, 50,5,5, fill="Red")
v1=vermelho.create_text(27, 27, text=tav, font="ProximaNova 15")
with open("fichas verdes", "r") as arquivove1:
    tave=arquivove1.read()

verde=Canvas(janela)
verde.place(x=318,y=145)
ve=verde.create_oval(50, 50,5,5, fill="Green")
ve1=verde.create_text(27, 27, text=tave, font="ProximaNova 15")
with open("fichas azuis", "r") as arquivoa1:
    taa=arquivoa1.read()

azul=Canvas(janela)
azul.place(x=182,y=196)
a=azul.create_oval(50, 50,5,5, fill="Blue")
a1=azul.create_text(27, 27, text=taa, font="ProximaNova 15", fill="White")
with open("fichas pretas", "r") as arquivop1:
    tap=arquivop1.read()
preto=Canvas(janela)
preto.place(x=182+90,y=196)
p=preto.create_oval(50, 50,5,5, fill="Black")
p1=preto.create_text(27, 27, text=tap, font="ProximaNova 15", fill="White")
def contabilizar():
    janelacont=Tk()
    janelacont.geometry("150x150")
    entbra=Entry(janelacont)
    entbra.insert(0, "Fichas BRANCAS")
    entbra.pack()
    entver=Entry(janelacont)
    entver.insert(0, "Fichas VERMELHAS")
    entver.pack()
    entved=Entry(janelacont)
    entved.insert(0, "Fichas VERDES")
    entved.pack()
    entaz=Entry(janelacont)
    entaz.insert(0, "Fichas AZUIS")
    entaz.pack()
    entpre=Entry(janelacont)
    entpre.insert(0, "Fichas PRETAS")
    entpre.pack()
    def pega():
        fichbra=entbra.get()
        fichbra=int(fichbra)
        with open("fichas brancas", "w") as arquivob:
                arquivob.write(fichbra)
        fichver = entver.get()
        with open("fichas Vermelhas", "w") as arquivov:
                arquivov.write(fichver)
        fichved = entved.get()
        with open("fichas verdes", "w") as arquivove:
                arquivove.write(fichved)
        fichazu = entaz.get()
        with open("fichas azuis", "w") as arquivoa:
                arquivoa.write(fichazu)
        fichpre = entpre.get()
        with open("fichas pretas", "w") as arquivop:
                arquivop.write(fichpre)

    pegarficha=Button(janelacont, text="CONTABILIZAR", command=pega)
    pegarficha.pack()



    janelacont.mainloop()

betap=Entry(janela)
betap.insert(0, "Sua Aposta")
betap.place(x=382, y=150, height=30, width=124)
def betdef():
    betus=int(betap.get())
    der= str(qtd-betus)
    der2 = str(qtd - 2*betus)
    der4 = str(qtd - 4* betus)
    emp = str(qtd+ 0)
    vit = str(qtd + betus)
    vit2 =str(qtd + 2*betus)
    vit4 = str(qtd + 4* betus)
    janelabet=Tk()



    janelabet.geometry("120x200")
    def per():
        with open("mymoney", "w") as plan:
            plan.write(der)
        dinheiro.configure(text=der)
        with open("vitorias", "a") as fim:
            fim.write(f"Derrota -{betus}\n")
    botde=Button(janelabet, text="Derrota", command=per)
    botde.pack()
    def per2():
        with open("mymoney", "w") as plan1:
            plan1.write(der2)
        dinheiro.configure(text=der2)
        with open("vitorias", "a") as fim1:
            fim1.write(f"Derrota -{betus*2}\n")
    botde2=Button(janelabet, text="Derrota X2", command=per2)
    botde2.pack()
    def per4():
        with open("mymoney", "w") as plan2:
            plan2.write(der4)
        dinheiro.configure(text=der4)
        with open("vitorias", "a") as fim2:
            fim2.write(f"Derrota -{betus*3}\n")
    botde4=Button(janelabet, text="Derrota X4", command=per4)
    botde4.pack()
    def dec():
        with open("mymoney", "w") as plan3:
            plan3.write(emp)
        with open("vitorias", "a") as fim3:
            fim3.write("Empate \n")
        dinheiro.configure(text=emp)
    botem=Button(janelabet, text="Empate",command=dec)
    botem.pack()
    def gan():
        with open("mymoney", "w") as plan4:
            plan4.write(vit)
        dinheiro.configure(text=vit)
        with open("vitorias", "a") as fim4:
            fim4.write(f"Vitoria +{betus}\n")
    botvi=Button(janelabet, text="Vitoria",command=gan)
    botvi.pack()
    def gan2():
        with open("mymoney", "w") as plan5:
            plan5.write(vit2)
            with open("vitorias", "a") as fim5:
                fim5.write(f"Vitoria +{betus*2}\n")
        dinheiro.configure(text=vit2)
    botvi2=Button(janelabet, text="Vitoria X2",command=gan2)
    botvi2.pack()
    def gan4():
        with open("mymoney", "w") as plan6:
            plan6.write(vit4)

        dinheiro.configure(text=vit2)
        with open("vitorias", "a") as fim6:
            fim6.write(f"Vitoria +{betus*4}\n")
    botvi4=Button(janelabet, text="Vitoria X4",command=gan4)
    botvi4.pack()
    janelabet.mainloop()
apobet=Button(janela, text="Aposte", font="ProximaNova 25", command=betdef)
apobet.place(x=382, y=190, height=67, width=124)
fichas=Button(janela, text="Suas fichas",font="ProximaNova 15", command=contabilizar )
fichas.place(x=11,y=227,height=30, width=124)



#saber posição
def clique(retorno):
    print(f'x:{retorno.x} / y : {retorno.y} geo :{janela.geometry()}')
janela.bind('<Button-3>', clique)


janela.mainloop()