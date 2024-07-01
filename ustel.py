def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1) #2*2*2*2*1 diyor ve return ediyor

a=int (input("tabanı giriniz:"))
b=int (input("üssü giriniz:")) #istediğimiz herhangi bir sayıyı bizden alıp yapacak

print(ustel(a,b))
