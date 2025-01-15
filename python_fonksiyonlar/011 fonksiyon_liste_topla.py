# Bir listenin içindeki tüm elemanları 
# toplayıp sonucu döndüren fonksiyon yazınız
def listeTopla(liste):
    toplam=0
    for i in range(0,len(liste)):
        toplam+=liste[i]
    return toplam

# Şimdi fonksiyonu çağıralım
a=[10,20,30,40] # a listemiz
b=[2,4,6,8,10] # b listemiz
print(listeTopla(a)) # 100 yazar
print(listeTopla(b)) # 30 yazar
