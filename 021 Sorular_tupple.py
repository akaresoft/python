#Tupple(demet)
# içeriği sadece okunabilir, değiştirilemez veri tipidir

defter=("kareli","çizgili","düz")
print(defter)

#defter(1)="ajanda"

defter_list=list(defter) #defteri listeye çeviriyoruz
print("defter_list Veri tipi:",type(defter_list)) # <class 'list'>
defter_list[1]="ajanda"
print(defter_list) #['kareli', 'ajanda', 'düz']

defter=tuple(defter_list)
print("Veri tipi:",type(defter)) #Veri tipi: <class 'tuple'>
print(defter)

#ilk 2 elemanı ekrana yazdırınız
print(defter[0:2])
#tupple'a 2 yeni eleman ekleyiniz
# defter.append("çizgisiz") #çalışmaz, tuple içeriği değiştirilemez
defter2=list(defter)
defter2.append("çizgisiz")
defter2.append("karesiz")
defter=tuple(defter2)
print(defter)
#sondan iki elemanı ekrana yazdırınız
print(defter[3:]) 