kelime=input("Kelime giriniz")

for i in range(len(kelime)):
    satir=""
    for j in range(len(kelime)):
        satir=satir+kelime[i]
    print(satir)