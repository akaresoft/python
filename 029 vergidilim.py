#Yıllık geliriniz 110 bin TL'ye kadar ise vergi oranınız %15
#230 bin TL’ye kadar ise 110 bin TL'lik kısmı için 16 bin 500 TL, üzerindeki tutarlar için %20
#580 bin TL’ye kadar ise 230 bin TL’lik kısmı için 40 bin 500 TL, üzerindeki tutarlar için %27
#3 milyon TL'ye kadar ise 580 bin TL’lik kısmı için 135 bin TL, üzerindeki tutarlar için %35
#Daha yüksek tutarlarda ise 3 milyon TL’lik kısım için 982 bin TL, üzerindeki tutarlar için ise %40 olarak hesaplanır.

k=float(input("Kazancınızı giriniz:"))
if (k<=110000):
    vergi=k*0.15
elif(k>110000 and k<=230000):
    vergi=(k-110000)*0.20+16500
elif(k>230000 and k<=580000):
    vergi=(k-230000)*0.27+40500
elif(k>580000 and k<=3000000):
    vergi=(k-580000)*0.35+135000
elif(k>3000000):
    vergi=(k-3000000)*0.40+982000
print("Vergi:",vergi) 