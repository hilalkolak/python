#def dolar(TL):
    #return(TL/32.27)

dolar=lambda TL: TL/32.27

TL=int(input("Türk lirası giriniz:"))
print(TL,"Türk Lirası=",dolar(TL),"Dolar")
