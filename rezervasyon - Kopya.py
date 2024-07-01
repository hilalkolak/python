masaNo=0
liste=['Ali','Can','Miray','Zeynep']
liste2=['Bahar','Talat']
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
elif isim in liste2:
    print("Rezervasyonunuz bu akşam değil")
elif isim not in liste and isim not in liste2:
    print ("Rezervasyonunuz yok")