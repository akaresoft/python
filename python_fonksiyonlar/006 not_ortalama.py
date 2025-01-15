def ortalamaBul(n1,n2,n3):
    ortalama=(n1+n2+n3)/3
    return ortalama

# şimdi ortlama fonksiyonunu 
# klavyeden üç değer alıp çağıralım

not1= float(input("1. notu giriniz:"))
not2= float(input("2. notu giriniz:"))
not3= float(input("3. notu giriniz:"))

sonuc=ortalamaBul(not1,not2,not3)
print("Notların ortalaması:",sonuc)