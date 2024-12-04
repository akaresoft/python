satirsay=int(input("Kaç satır olacak:"))

for i in range(satirsay):
    satir=""
    for j in range(i+1):
       satir+="*"
    print(satir)