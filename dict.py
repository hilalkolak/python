gun=input("Türkçe gün adı..:")
TrEn={'pazartesi':'monday','salı':'tuesday','çarşamba':'wednesday','perşembe':'thursday','cuma':'friday','cumartesi':'saturday','pazar':'sunday'}
print("ingilizcesi..:",end=" ")
print(TrEn.get(gun,'Bu kelime sözlükte yok!'))
