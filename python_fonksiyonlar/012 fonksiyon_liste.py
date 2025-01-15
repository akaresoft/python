# liste şeklinde gönderilen notların harf karşılıklarını döndürünüz
def harfNotuBul(x):
    harf=""
    if(0<x<40):      harf="F"   # if(x>0 and x<40): harf="F"
    elif(40<=x<55):  harf="D" 
    elif(55<=x<70):  harf="C"
    elif(70<=x<85):  harf="B"
    elif(85<=x<=100):harf="A"
    else:            harf="Z" #aralık dışı
    return harf

#listeCevir fonksiyonu bir listeyi alarak harf notuna çevirip döndürür.
def listeCevir(notlar):
    harfNotlar=[]
    for i in range(0,len(notlar)):
        harfNotlar.append(harfNotuBul(notlar[i]))
    return harfNotlar

liste=[20,30,40,45,50,55,70,80,90]
print(listeCevir(liste)) #['F', 'F', 'D', 'D', 'D', 'C', 'B', 'B', 'A']
