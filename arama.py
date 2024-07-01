L=[12,23,45,56,78,89]
deger=int(input('sayı giriniz..:'))
if deger in L:
    indis=L.index(deger)
    print("Aranan",indis,"indis değerinde bulundu")
else:
    print("aranan değer bulunmadı!")

    
