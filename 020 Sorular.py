#listeler
teksayi=[5,7,9,11,13,15]
print(teksayi)

ciftsayi=[6,8,10,12,14,16]
print(ciftsayi)

sayilar=ciftsayi, teksayi
print(sayilar)
ciftsayi.append(100) #sayilar.append(100) çalışmaz
print(sayilar)
print(sayilar[0][2]) #10 yazar
print(sayilar[1][3]) #11 yazar
print(sayilar[0][1:3]) #8,10 yazar
print(sayilar[1][2:4]) #9,11 yazar
print(sayilar[0][:-2]) #6,8,10,12,14 yazar
print(sayilar[1][-3:-1]) #11, 13 yazar
print(sayilar[1][:])
print(sayilar[0][0:5:2])