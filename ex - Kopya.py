import time
import os

def alarm_cal(muzikDosya):
    os.system(f"start {muzikDosya}")

def pomodoro_zamanlayici(durum, sure, muzikDosya):
    print(f"{durum} zamanı!")
    if muzikDosya:
        alarm_cal(muzikDosya)
        time.sleep(10)  # Müziği 10 saniye çal, sonra durdur
    time.sleep(sure)

# Her bir müzik dosyası için çalma durumu (çalındıysa True, çalmadıysa False)
calindi = {"calisma": False, "mola": False}

# Çalışmanın başlangıç saati
baslangic_saati = 9

# Günde 8 kez çalışma ve mola döngüsü
for _ in range(8):
    # Öğle arası kontrolü
    if baslangic_saati == 12:
        time.sleep(60 * 60)  # Öğle arası için 1 saat bekleyin
        baslangic_saati = 13  # Öğle arasından sonra çalışmaya 13'te devam edin
    
    if not calindi["calisma"]:
        pomodoro_zamanlayici("Çalışma", 55 * 60, "break_end.mp3")  # 55 dakika sürsün, çalışma için müzik
        calindi["calisma"] = True
    else:
        calindi["calisma"] = False
    
    if not calindi["mola"]:
        if baslangic_saati == 13:
            pomodoro_zamanlayici("Mola", 5 * 60, "work_end.mp3")  # 5 dakika sürsün, öğle molası için müzik
            calindi["mola"] = True
        else:
            pomodoro_zamanlayici("Mola", 5 * 60, "break_end.mp3")  # 5 dakika sürsün, sabah/masaüstü molası için müzik
            calindi["mola"] = True
    else:
        calindi["mola"] = False
    
    baslangic_saati += 1  # Sonraki çalışmanın başlangıç saati


