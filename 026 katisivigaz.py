s=float(input("Sıcaklık giriniz:"))

if(s<=0):
    print("Katı-buz halde")
elif(0<s<100):
    print("Sıvı halde")
elif(s>=100):
    print("Gaz halinde")