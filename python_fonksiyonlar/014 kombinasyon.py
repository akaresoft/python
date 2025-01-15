# faktöriyel hesaplama
def faktoriyel(n):
    if (n==0):
        return 1
    elif(n>0):
        fakt=1
        for i in range(1,n+1):
            fakt*=i
        return fakt

# kombinasyon hesaplama
def kombinasyon(n,r):
    # (n!)/(r!*(n-r)!)
    sonuc= faktoriyel(n)/faktoriyel(r)*faktoriyel(n-r)
    return sonuc

n=3
r=2
print(kombinasyon(n,r))