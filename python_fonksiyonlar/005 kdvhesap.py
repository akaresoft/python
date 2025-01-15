def kdvhesap(kdvOran, fiyat):
    satisFiyat= fiyat + fiyat*kdvOran/100
    return satisFiyat

#şimdi kdvhesap fonksiyonunu çağıralım
# bu fonksiyon iki parametre alıyor
# kdvOran ve fiyat değerlerini gönderiyoruz
# hesaplayıp bize satış fiyatını döndürüyor

oran=20
f=200
print(kdvhesap(oran,f))