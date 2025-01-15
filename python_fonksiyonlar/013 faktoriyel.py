# Girilen bir sayının faktöriyelini bulan fonksiyon yazınız
# 0!=1
# 2!= 2.1=2
# 3!= 3.2.1=6
# 4!= 4.3.2.1=24
def faktoriyel(n):
    if (n==0):
        return 1
    elif(n>0):
        fakt=1
        for i in range(1,n+1):
            fakt*=i
        return fakt


sayi=int(input("Faktöriyeli alınacak sayı:"))
sonuc=faktoriyel(sayi)
print("Faktöriyel sonucu:",sonuc)

