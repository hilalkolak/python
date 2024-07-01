import random
sayi=random.randint(1,6)
tahmin=int(input("Tahmin et..:"))
skor=5
while True:
    if sayi==tahmin:
        print("Kazandınız..:) Skorunuz..:",skor)
        break
    else:
        print("Olmadı..:( Skorunuz..:",skor)
        skor-=1
        tahmin=int(input("Tahmin et..:"))
