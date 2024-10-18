liste=['kurşun kalem','defter','silgi','çanta']
uzunluk=len(liste)
print("Liste uzunluğu",uzunluk)

liste.append("dolma kalem") #sona eleman ekler
#print(liste)
liste.insert(2,'pergel') #araya eleman ekler 
#'kurşun kalem', 'defter', 'pergel', 'silgi', 'çanta', 'dolma kalem'
#print(liste)
liste.remove('silgi') #silgi elemanını siler
#print(liste) #['kurşun kalem', 'defter', 'pergel', 'çanta', 'dolma kalem']

liste.remove(liste[2]) # yeni listeden 3.elemanı kaldırır
#print(liste) #['kurşun kalem', 'defter', 'çanta', 'dolma kalem']

liste.pop(0) #belirtilen index'teki elemanı siler
#print(liste) #['defter', 'çanta', 'dolma kalem']

print(liste.index('çanta'))
liste.append('sulu boya')
liste.append('şemsiye')
liste.append('sulu boya')
#print(liste)
print("Kaç tane sulu boya var?",liste.count('sulu boya'))

liste.sort() # sıralama yapar
#print(liste)

liste.reverse() #listeyi ters çevirir
#print(liste)

yeniliste= liste.copy()
print(yeniliste)

liste2=['matara','bardak','tabak']
liste.extend(liste2) #liste'yi liste2 ile genişletelim
print(liste)

del liste[1] #belirtilen index'teki elemanı siler
#print(liste)

malzeme=['çekiç','tornavida','çivi']
malzeme2=[malzeme,'vida','somun','kerpeten','yan keski']
print(malzeme2)

#liste.clear() #bütün elemanları siler
#print(liste)
