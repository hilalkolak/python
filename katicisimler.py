from math import *

class kup:  #kup sınıfı
    def __init__(self,a):
        self.a=a

    def yAlan(self):
        return("yuzey alanı..:",6*pow(self.a,2),"cm^2")

    def hacim(self):
        return(pow(self.a,3))

class kure: #kure sınıfı
    def __init__(self,r):
        self.r=r

    def yAlan(self):
        return("yüzey alanı..:",4*pi*pow(self.r,2),"cm^2 dir")

    def hacim(self):
        return ("hacim..:",(4/3)*pi*pow(self.r,3),"cm^3")

class silindir: #silindir sınıfı
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def yALan(self):
        return("yüzey alanı..:",2*pi*self.r(self.r+self.h),"cm^2") #(2*pi*pow(r,2)) + (2*pi*r*h)

    def hacim(self):
        return ("hacim..:",pi*pow(self.r,2)*self.h,"cm^3")

futbolTopu=kure(10) #futbol topu nesnesi class kure (yarı çapı)
pinponTopu=kure(3)  #pinpon topu nesnesi class kure

kupSeker=kup(2)     #kup şeker nesnesi class kup
koli=kup(50)        #koli nesnesi class silindir

merdane=silindir(3,30)  #merdane nesnesi class silindir
tencere=silindir(15,20) #tencere nesnesi class silindir
lastik=silindir(35,20)  #lastik nesnesi class silindir
