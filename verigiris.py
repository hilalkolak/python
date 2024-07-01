from turtle import *
N=int(numinput("poligon","kenar sayısı",5)) #kullanıcıdan sayısal bir değer alıyor bu sayısal bir değer oluyor float tpinde oluyor bunu intiger e cevirmem lazım
renk=textinput("renk","dolgu rengi")

pensize(4)


begin_fill()
fillcolor(renk)
circle(100,360,N)
end_fill()
