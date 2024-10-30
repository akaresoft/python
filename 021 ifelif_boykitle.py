kilo= float(input("Kilonuzu giriniz:"))
boy= float(input("Boyunuzu giriniz:"))
bki=kilo/(boy**2)
print("BKİ=",bki)
if(bki<20):
    print("Zayıf")
elif(20<=bki<25):
    print("Normal")
elif(25<=bki<30):
    print("Hafif şişman")
elif(30<=bki<35):
    print("Şişman")
elif(35<=bki<45):
    print("Sağlık açısından önemli")
elif(45<=bki<50):
    print("Aşırı şişman")
elif(bki>=50):
    print("Morbid")

