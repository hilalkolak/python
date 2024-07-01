import datetime
class araba:
    def __init__(self,model,fiyat):
        self.model=model
        self.fiyat=fiyat
    def arabaBilgi(self):
        print("araba modeli:",self.model,"\n","araba fiyatı:",self.fiyat)
        return(datetime.datetime.now())

class kamyon(araba):
    def __init__(self,model,fiyat,renk):
        araba.__init__(self,model,fiyat)
        self.renk=renk

k1=kamyon(2020,120000,"kırmızı")
k1.arabaBilgi()



