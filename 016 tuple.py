#tuple(demet) veri tipi, liste gibidir, fakat elemanları değiştirilemez
mevsimler=('ilkbahar','yaz','sonbahar','kış','ilkbahar')

# liste gibi index parametreleri ile tuple elemanlarına ulaşabilirsiniz
print(mevsimler)
print("İlk mevsim:",mevsimler[0])
print("Son mevsim:",mevsimler[-1]) #son elemana ulaşım
# mevsimler[0]='XXX'  #hata verir, tuple'a atama yapılamaz
elemanSayisi= len(mevsimler)
print('Eleman Sayısı:',)

#bir elemandan kaç adet olduğunu bulmak için count kullanıyoruz
say= mevsimler.count('ilkbahar')
print('Tuple içinde İlkbahar sayısı:',say)

#LİSTEYE ÇEVRİM
mevsimler_list= list(mevsimler) #tuple'dan listeye çevirim, yoksa içindekileri değiştiremeyiz
mevsimler_list[0]="spring"
mevsimler_list[1]="summer"
mevsimler_list[2]="autumn"
mevsimler_list[3]="winter"
print("Bütün liste:",mevsimler_list)

sirano=mevsimler.index("yaz")
print("Yaz elemanının sıra numarası:",sirano)

sirano=mevsimler.index("XXX")
print("XXX elemanının sıra numarası:",sirano)