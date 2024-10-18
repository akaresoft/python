fiyat = float(input("Fiyat giriniz:"))
kdv= float(input("Kdv yüzdesini giriniz:"))

satis= fiyat + fiyat*kdv/100
print("Satış fiyatı:",satis)