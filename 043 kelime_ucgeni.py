# girilen bir kelimenin her bir harfini tekrar ettiriniz
# Örneğin KAŞ kelimesi
# K
# AA
# ŞŞŞ
kelime=input("Kelime giriniz :")
sayac=0
for i in range(len(kelime)):
    sayac+=1
    satir=""
    for j in range(sayac):
        satir=satir+kelime[i]
    print(satir)