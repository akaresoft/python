
# Dictionary(sözlük) veri tipi key(anahtar):value(değer) şeklinde
# veri saklayan bir veri tipidir.

sehirler={
          34:"İstanbul",
          6:"Ankara",
          35:"İzmir",
          63:"AAA" ,
          23:"BBB"
           } #JSON veri formatına çok benzer, bu format veri işlemlerinde çok kullanılır
print(sehirler) #{34: 'İstanbul', 6: 'Ankara', 35: 'İzmir'}
print(sehirler[34]) # İstanbul yazar
print(sehirler[6]) # Ankara yazar
print(sehirler.keys()) #dict_keys([34, 6, 35])
print(sehirler.values()) #dict_values(['İstanbul', 'Ankara', 'İzmir'])

sehirler[63]="Şanlıurfa" #değerlerini değiştiriyoruz
sehirler[23]="Elazığ" #değerlerini değiştiriyoruz
print(sehirler)

print("Uzunluk:",len(sehirler))
sehirler.pop(63) #pop metodu ile 63 anahtarlı Şanlıurfa silinir
print(sehirler)

sehirler_yedek= sehirler.copy()
print("Yedek şehirler",sehirler_yedek)
sehirler.clear() # clear metodu ile sehirler'in içini boşaltıyoruz
print(sehirler)

#del sehirler #sözlüğü tamamen siliyoruz
#print(sehirler) #hata verir