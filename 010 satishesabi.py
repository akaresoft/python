satis = float(input("Satış fiyatı giriniz:"))
kdv= float(input("Kdv yüzdesini giriniz:"))
fiyat= 100*satis/(100+kdv)

print("Alış Fiyatı:",fiyat)