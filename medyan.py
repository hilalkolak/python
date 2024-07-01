L=[]
for i in range(0,6):
    sayi=int(input('Sayı giriniz..:'))
    L.append(sayi)
L.sort()
print('Listenin medyanı',(L[2]+L[3])/2)

