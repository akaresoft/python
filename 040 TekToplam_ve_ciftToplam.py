# aşağıdaki listede 10'dan büyük sayıların ortalamasını bulunuz
dizi=[3,4,5,11,12,20,21,8,31,6,43,22,32]

tekToplam=0
ciftToplam=0
tekSayac=0
ciftSayac=0

for i in range(len(dizi)):
 if (dizi[i]%2==0):
  ciftToplam+=dizi[i]
  ciftSayac+=1
 else:
  tekToplam+=dizi[i]
  tekSayac+=1

tekOrt=tekToplam/tekSayac
ciftOrt=ciftToplam/ciftSayac
print("Çift toplam:",ciftToplam)
print("Tek Toplam:",tekToplam)
print("Çift Ortalama:",ciftOrt)
print("Tek Ortalama:",tekOrt)



