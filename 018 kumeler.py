#KÜMELER (SETS)
markalar={"bmw","mercedes","togg"}
print(markalar)

print("togg" in markalar) #True "togg" markası markalar kümesinde var
print("vw" in markalar)# False "vw" markası kümede yok

markalar.add("audi") #audi'yi kümeye ekleyelim
print(markalar)

markalar.update(["ferrari","bentley","porsche"])
print(markalar) #{'bmw', 'togg', 'ferrari', 'audi', 'bentley', 'porsche', 'mercedes'}
markalar.discard("mercedes") #verilen index teki elemanı siler
print(markalar)
