# aşağıdaki listede 10'dan büyük sayıların ortalamasını bulunuz
dizi=[3,4,5,11,12,20,8,6,22,32]

toplam=0
sayac=0
for i in range(len(dizi)):
 if(dizi[i]>=10):
  sayac+=1
  toplam+=dizi[i]

ortalama=toplam/sayac
print("Toplam  :",toplam)
print("Ortalama:",ortalama)
