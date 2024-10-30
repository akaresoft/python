agac=["zeytin","çınar","gürgen","kestane"]
print(agac)

agac.append("palamut")
print(agac)
agac.append("çınar")
print("Çınar ağacı listede",agac.count("çınar"),"adet var")

agac2=["ceviz","fındık"]
agac.extend(agac2)
print("Genişletilmiş agac listesi:",agac)

ceviz_sira_no=agac.index("ceviz")
print("Ceviz sira no:",ceviz_sira_no)

agac.insert(1,"kiraz") # 1 nolu indekse kiraz eklenir, sonrakiler sağa kayar
print(agac)

agac.pop(-1) #en sondaki elemanı çıkarıyoruz
print("Son eleman silindikten sonra",agac) #dındık silindi

agac.pop(0) #ilk elemanı sileriz
print("0 nolu index silindikten sonra",agac) #zeytin silindi

agac.remove("gürgen")
print(agac)

agac.sort() #Türkçe karakterlere göre sıralamaz
print("Sıralama sonucu:",agac) 

agac.reverse()
print("Ters çevrilince:",agac)

agacyedek=agac.copy() #agac listesinin kopyasını agacyedek'e aktarır
print(agacyedek)

agac.clear() #agac listesini siler
print(agac) # [] boş liste döndürür
