benzinfiyat = float(input("Benzin litre fiyatını giriniz:"))
aracharcama= float(input("Aracınız 100 km de  yüzdesini giriniz:"))
mesafe=  float(input("Km olarak mesafe giriniz:"))

odenecek= (benzinfiyat*aracharcama/100)*mesafe
print("Ödenecek:", odenecek)
