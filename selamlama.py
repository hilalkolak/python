def selamlama(isim):
    print("Sayın",isim,"Restoranımıza hoşgeldiniz")
while True:
    Ad=input("İsminiz nedir?")
    if(Ad=="dur"):
       break
    selamlama(Ad) #dur isminde biri gelene kadar program çalışmaya devam edecek
