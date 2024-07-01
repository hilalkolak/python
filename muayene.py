L=[]                               #boş liste
while True:                        #sonsuz döngü
    TC=int(input("TC gir..:"))  
    if TC in L:                    # TC listenin içide varsa muayene sırası soracak
        i=L.index(TC)
        print("Muayene Sırası..:",i+1) #muayene sırası
    elif TC==0:                    #doktor içeriden hasta çağırıyor
        print(L[0],'TC numaralı hasta doktorun yanına gidiniz.')                #sıra kimde
        L.pop(0)                   #kuyruktan atmak için
    else:                          #kişi listede yok,yeni gelmiş bir hata ve kaydedilmiş
        L.append(TC)               #kişi tc ile kendini sıraya sokmak istiyor.
        print(TC,'TC numaralı hasta sıraya alındı.')
