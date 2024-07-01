L=[]
while True:
    isim=input('İsim giriniz..:')
    L.append(isim)
    if isim=='sıradaki':
        print(L.pop(0))
    if isim=='bitti':
        break
    
