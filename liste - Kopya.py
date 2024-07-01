masaNo=0
liste=['Ali','Can','Miray','Zeynep']
isim=input('İsminiz nedir?..')
if isim=='Ali':
    masaNo=5
if isim=='Can':
    masaNo=7
if isim=='Miray':
    masaNo=2
if isim=='Zeynep':
    masaNo=10
if isim in liste:
    print(masaNo,"Numaralı masada rezervasyonunuz var")
if isim not in liste:
    print ("Rezervasyonunuz yok")