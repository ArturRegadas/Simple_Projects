from datetime import date
dia=date.today().day

mes=date.today().month

ano=date.today().year

codfont=dia+mes+ano
if (codfont+dia)&2==1:
    codfont=codfont+509243422
    codfont1=(dia%2)*3
    codfont2=dia+mes
    codfont=str(codfont)
    codfont1=str(codfont1)
    codfont2=str(codfont2)
else:
    codfont=codfont+82611214
    codfont1=(codfont*3)%2*4%2*2
    codfont2=(codfont1+codfont)%2*3

    codfont=str(codfont)
    codfont1=str(codfont)
    codfont2=str(codfont2)
print(codfont+codfont1+codfont2)