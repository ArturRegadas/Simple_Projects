from tkinter import *
from ttkthemes import *
import tkinter.ttk as tk
import tkinter.font
import requests
requizicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
requizicao_dic = requizicao.json()

requizicao1 = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD,EUR-USD,BTC-USD,ETH-USD")
requizicao_dic1 = requizicao1.json()
requizicao2 = requests.get("https://economia.awesomeapi.com.br/last/BRL-EUR,USD-EUR,BTC-EUR,ETH-EUR")
requizicao_dic2 = requizicao2.json()
requizicao3 = requests.get("https://economia.awesomeapi.com.br/last/BRL-BTC,USD-BTC,EUR-BTC,ETH-BTC")
requizicao_dic3 = requizicao3.json()
requizicao4 = requests.get("https://economia.awesomeapi.com.br/last/BRL-ETH,USD-ETH,EUR-ETH,BTC-ETH")
requizicao_dic4 = requizicao4.json()
#para real
cotacaou_R=requizicao_dic["USDBRL"]["bid"]

cotacaoe_R=requizicao_dic["EURBRL"]["bid"]

cotacaob_R=requizicao_dic['BTCBRL']['bid']

cotacaoet_R=requizicao_dic["ETHBRL"]['bid']

#para dolar
cotacaor_U=requizicao_dic1["BRLUSD"]["bid"]
cotacaoe_U=requizicao_dic1["EURUSD"]["bid"]
cotacaob_U=requizicao_dic1['BTCUSD']['bid']
cotacaoet_U=requizicao_dic1["ETHUSD"]['bid']

#para euro
cotacaor_E=requizicao_dic2["BRLEUR"]["bid"]
cotacaou_E=requizicao_dic2["USDEUR"]["bid"]
cotacaob_E=requizicao_dic2['BTCEUR']['bid']
cotacaoet_E=requizicao_dic2["ETHEUR"]['bid']







janela=ThemedTk(theme='breeze')
#janela.iconbitmap(default='iconetp.ico')
janela.title('KGL Bank')
janela.geometry('1280x720')
janela.resizable(False, False)



pngl= PhotoImage(file='Design sem nome (3).png')
pngl1=PhotoImage(file="Design sem nome (4).png")
pngl2=PhotoImage(file="Inserir um pouquinho de texto.png")
labelpng=Label(janela, image=pngl)
labelpng.pack()


#Saber posição
def clique(retorno):
    print(f'x:{retorno.x} / y : {retorno.y} geo :{janela.geometry()}')
janela.bind('<Button-3>', clique)

#comandos

def comando1():
    janela1= Tk()
    janela1.geometry("400x300")
    janela1.resizable(False, False)

    entrcn = Entry(janela1,font='ProximaNova 16 ',fg="#848080" , background='#DFDFDF', relief="flat" )
    entrcn.insert(0, "new user")
    entrcn.place(x=15, y = 15,width=365 , height=53 )
    entrcn2 = Entry(janela1,font='ProximaNova 16 ',fg="#848080" , background='#DFDFDF', relief="flat")
    entrcn2.insert(0, "senha")
    entrcn2.place(x=15, y = 100,width=365 , height=53 )

    def criarc():
        novauser=entrcn.get()
        novauser=str(novauser)
        novasenha=entrcn2.get()
        novasenha = str(novasenha)

        with open("banco.txt", "a") as file:
            file.write("\n" + novauser)
            file.write("\n" + novasenha)


    butcn=Button(janela1,text="Criar conta",font='ProximaNova 33 ',fg="#848080" , background='#FF834F', relief="flat",command=criarc)
    butcn.place(x=15, y = 200,width=365 , height=90 )


    janela1.mainloop()



#Entry's

entryl1 = Entry(janela, font='ProximaNova 21 ',fg="#848080" , background='#DFDFDF', relief="flat")
entryl1.insert(0, "User ID")
entryl1.place(x=450 , y=354, width=493 , height=53)

entryl2 = Entry(janela, font='ProximaNova 21 ',fg="#848080" , background='#DFDFDF', relief="flat", show = "*")
entryl2.insert(0, "senha")
entryl2.place(x=450 , y=438, width=493 , height=53)
x=0

def logar():
    logar1 = entryl1.get()
    logar1 = str(logar1)
    logar2 = entryl2.get()
    logar2 = str(logar2)
    l1=0
    with open("banco.txt", 'r') as file:
        if logar1 + "\n" in file:
            if logar2  in file:
                entryl1.destroy()
                entryl2.destroy()
                botao.destroy()
                botao2.destroy()
                checkb1.destroy()
                labelpng.configure(image=pngl1)

                def conversor():

                    janelaconversor=Tk()
                    janelaconversor.title('KGL Conversor')
                    janelaconversor.geometry('700x400')
                    janelaconversor.resizable(False, False)
                    labelcon=LabelFrame(janelaconversor, text="")
                    labelcon.place(x=25, y=196, width=300, height=175)
                    labelcon1=LabelFrame(janelaconversor, text="")
                    labelcon1.place(x=375, y=196, width=300, height=175)

                    combo = tk.Combobox(janelaconversor, state= 'readonly',)
                    combo['values'] = ('Dolar', 'Euro', 'BitCoin', 'Ethereum', "Reais_brasileiros")
                    combo.current(0)
                    combo.place(x=25, y=196, width=300, height=30)
                    combo1 = tk.Combobox(janelaconversor, state= 'readonly',)
                    combo1['values'] = ('Dolar', 'Euro', "Reais_brasileiros")
                    combo1.current(0)
                    combo1.place(x=375, y=196, width=300, height=30)

                    entradaconv=Entry(janelaconversor, font="Arial 40",  relief="flat")
                    entradaconv.insert(0, "1")
                    entradaconv.place(x=26, y=226, width=296, height=143)

                    Lvel=Label(janelaconversor, text="", font="Arial 40",  relief="flat", bg="White")
                    Lvel.place(x=376, y=226, width=296, height=143)

                    def converter():

                        cd=combo.get()
                        cd1=combo1.get()
                        end=entradaconv.get()
                        end=float(end)



                        if cd == cd1:

                            Lvel.configure(text=end)

                        if cd == "Reais_brasileiros" and cd1 =="Dolar":

                            convertido=end*float(cotacaor_U)
                            Lvel.configure(text=convertido)

                        if cd == "Reais_brasileiros" and cd1 =="Euro":
                            convertido = end * float(cotacaor_E)
                            Lvel.configure(text=convertido)

                        if cd == "Dolar" and cd1 =="Euro":
                            convertido = end * float(cotacaou_E)
                            Lvel.configure(text=convertido)
                        if cd == "Dolar" and cd1 =="Reais_brasileiros":
                            convertido = end * float(cotacaou_R)
                            Lvel.configure(text=convertido)

                        if cd == "Euro" and cd1 == "Dolar":
                            convertido = end * float(cotacaoe_U)
                            Lvel.configure(text=convertido)
                        if cd == "Euro" and cd1 =="Reais_brasileiros":
                            convertido = end * float(cotacaoe_R)
                            Lvel.configure(text=convertido)
                        if cd == "BitCoin" and cd1 =="Dolar":
                            convertido = end * float(cotacaob_U)
                            Lvel.configure(text=convertido)
                        if cd == "BitCoin" and cd1 =="Euro":
                            convertido = end * float(cotacaob_E)
                            Lvel.configure(text=convertido)
                        if cd == "BitCoin" and cd1 =="Reais_brasileiros":
                            convertido = end * float(cotacaob_R)
                            Lvel.configure(text=convertido)
                        if cd == "Ethereum" and cd1 =="Dolar":
                            convertido = end * float(cotacaoet_U)
                            Lvel.configure(text=convertido)
                        if cd == "Ethereum" and cd1 =="Euro":
                            convertido = end * float(cotacaoet_E)
                            Lvel.configure(text=convertido)
                        if cd == "Ethereum" and cd1 =="Reais_brasileiros":
                            convertido = end * float(cotacaoet_R)
                            Lvel.configure(text=convertido)

                    botaoconvesao=Button(janelaconversor, text="Converter", font="Arial 40",  relief="flat",fg="#ff834f", command=converter)
                    botaoconvesao.place(x=220, y=30, width=260, height=80)

                    janelaconversor.mainloop()
                nbotao1=Button(janela, font= "Questrial 14 ", text='Conversor',fg= "#8A8A8A", background="#FFFFFF", relief='flat', command=conversor)
                nbotao1.place(x=20,y=140, width=120, height=27)


                def comprar():
                    janelacomprar=Tk()
                    janelacomprar.title('KGL Ações')
                    janelacomprar.geometry('1280x720')
                    janelacomprar.resizable(False, False)







                    janelacomprar.mainloop()

                nbotao2=Button(janela, font= "Questrial 14 ", text='Comprar',fg= "#8A8A8A", background="#FFFFFF", relief='flat',command=comprar)
                nbotao2.place(x=14,y=210, width=120, height=27)

                nbotao3=Button(janela, font= "Questrial 14 ", text='Empréstimo',fg= "#8A8A8A", background="#FFFFFF", relief='flat')
                nbotao3.place(x=28,y=280, width=120, height=27)


                nbotao4=Button(janela, font= "Questrial 14 ", text='Poupança',fg= "#8A8A8A", background="#FFFFFF", relief='flat')
                nbotao4.place(x=20,y=400, width=120, height=27)


                nbotao5=Button(janela, font= "Questrial 14 ", text='Novo dia   ',fg= "#8A8A8A", background="#FFFFFF", relief='flat')
                nbotao5.place(x=20,y=463, width=120, height=27)


                nbotao6=Button(janela, font= "Questrial 14 ", text='Sair           ',fg= "#8A8A8A", background="#FFFFFF", relief='flat', command=fechar)
                nbotao6.place(x=20,y=526, width=120, height=27)
                nbotao7=Button(janela, font= "Questrial 14 ", text='Condifgurações',fg= "#8A8A8A", background="#FFFFFF", relief='flat')
                nbotao7.place(x=15,y=610, width=143, height=27)

                butver1=Button(janela, font= "Questrial 14 ", text='ver mais',fg= "#FF834F", background="#FFFFFF", relief='flat')
                butver1.place(x=980,y=350, width=143, height=27)
                butver2=Button(janela, font= "Questrial 14 ", text='ver mais',fg= "#FF834F", background="#FFFFFF", relief='flat')
                butver2.place(x=980,y=635, width=143, height=27)
                butver3=Button(janela, font= "Questrial 14 ", text='Converter',fg= "#FF834F", background="#FFFFFF", relief='flat')
                butver3.place(x=700,y=425 , width=130, height=27)
                butverdia=Button(janela, font= "Questrial 30 ", text='Novo dia ',fg= "White", background="#ff834f", relief='flat')
                butverdia.place(x=318,y=327 , width=210, height=50)


                nbotao = Button(janela, font="Questrial 14 ", text='Ver conta', fg="#FF834F", background="#FFFFFF",
                                relief='flat')


                nbotao.place(x=17, y=77, width=120, height=27)
                with open("dinheiro.txt", 'r') as dinheiro:
                    for l in dinheiro:
                        l=l
                    Lablvar=int(l)
                with open("xp.txt", "r") as xp:
                    for x in xp:
                        x=x
                    lavxp = int(x)
                dxp=str(x)
                j=str(Lablvar)
                labell=Label(janela, text=j+"       ", bg="#ff9055", fg="#ffffff")
                Desired_font = tkinter.font.Font(family="Bahnschrift SemiBold Condensed",
                                                 size=43,
                                                 weight="bold")
                labell.configure(font=Desired_font)
                labell.place(x=428,y=205,height=45, width=167)

                labeln=Label(janela, text=logar1+"       ", bg="White", fg="Black", font="Arial 18")
                labeln.place(x=438, y=11, height=30, width=130)

                labeln2=Label(janela, text=logar1+" Silva Oliveira", fg="White", bg="#ff834f", font="Arial 13")
                labeln2.place(x=306, y=306, height=12, width=200)

                labeld3=Label(janela, text="    "+j+',00', fg="#2a2a2a", bg="White", font="Arial 13")
                labeld3.place(x=912, y=17, height=15, width=100)

                labeld4 = Label(janela, text="       "+dxp+"xp", fg="#2a2a2a", bg="White", font="Arial 13")
                labeld4.place(x=1075, y=15, height=15, width=100)

                labelr5 = Label(janela, text="R$"+cotacaou_R, fg="#2a2a2a", bg="White", font="Arial 13")
                labelr5.place(x=325, y=650, height=25, width=70)
                labelr6 = Label(janela, text="R$"+cotacaoe_R, fg="#2a2a2a", bg="White", font="Arial 13")
                labelr6.place(x=455, y=650, height=25, width=70)
                labelr7 = Label(janela, text="R$"+cotacaob_R, fg="#2a2a2a", bg="White", font="Arial 13")
                labelr7.place(x=585, y=650, height=25, width=75)
                labelr8 = Label(janela, text="R$"+cotacaoet_R, fg="#2a2a2a", bg="White", font="Arial 13")
                labelr8.place(x=715, y=650, height=25, width=85)



botao = Button(janela, font= "Questrial 33", text='Login',fg= "#FFFFFF", background="#FF834F", relief='flat',command=logar)
botao.place(x=380, y=564, width=581 ,height=80)

botao2 = Button(janela, font= "Questrial 14 underline", text='Criar Conta',fg= "#FF834F", background="#2a2a2a", relief='flat', command=comando1)
botao2.place(x=802,y=517, width=100, height=27)
#checbud
def fechar():
    janela.destroy()
checkb1=Button(janela, text="Sair",font= "Questrial 14 ",fg="#FF834F", background="#2a2a2a",  relief="flat",command=fechar)
checkb1.place(x=415, y=517, width=60, height=20)




janela.mainloop()
