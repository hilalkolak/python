kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

#1-'Btk Akademi' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.(strip)
sonuc ='Btk Akademi'.strip()
#2-kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
sonuc = kursAdi.lower()
#3- website değişkeni kaç tane '.' karakteri vardır
sonuc = website.count('.')
#4- website değişkeni 'https' ile mi başlıyor?
sonuc = website.startswith('https')
#5- website 'tr' ile mi bitiyor?
sonuc = website.endswith('tr')
#6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor?
sonuc = kursAdi.isalpha()
#7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiriniz.
sonuc = kursAdi.replace('','-').lower()
#8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
sonuc = kursAdi.replace('Python','ReactJs')
#9- website değişkeni 'www' içeriyor mu?
sonuc = website.find('www')
sonuc = website.index('www')
#10- kursAdi değişkenini listeye çeviriniz.
sonuc = kursAdi.split()

print(sonuc)

















