sifre='1234'
Kullanici='hilal'

K_giris=input('kullanıcı adı giriniz:')
if K_giris==Kullanici:
    S_giris=input('şifre giriniz:')
    if S_giris==sifre:
        print('hoşgeldiniz')
    else:
        print("şifre hatalı")
        
else:
    print("kullanıcı adı hatalı!!")

    
