class Araba():
    def __init__(self,model,marka,renk): #metot
        self.model=model
        self.marka=marka
        self.renk=renk
    def aracbilgisi(self):
        print("markası:",self.marka)
        print("model:",self.model)  #nesne metotu
        print("renk:",self.renk)

a=3

Taksi=Araba(2020,"FIAT","YEŞİL")
print(Taksi.model)
