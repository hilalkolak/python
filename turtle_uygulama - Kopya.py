from turtle import * #içiçe kare çizimi

def kareCizim(mesafe): #kare çizim fonksiyonu
    for a in range (1,5):
        forward(mesafe)
        left(90)

hideturtle()
pensize(2)
x=int(input("kare sayısı gir:")) #kullanıcıdan alma kodu
x+=1
for a in range(x):
    kareCizim(50*a)
