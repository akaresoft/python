
liste=[11,10,22,5,7,9,11,35,23]

aranan = int(input("Arananılacak sayı:"))
bulundu=False
for i in range(len(liste)):
    #print(liste[i]) # listenin elemanlarını ekrana yazdırıyoruz
    if(liste[i]==aranan):
        bulundu=True

#alttaki kısım döngü bittikten sonra çalışıyor
if (bulundu):
    print("Aranan ",aranan," listede var")
else:
    print('Aranan bulunamadı')
