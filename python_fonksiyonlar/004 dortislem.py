# toplam fonksiyonu
def topla(a,b):
    return (a+b)

# çarpım fonksiyonu
def carp(a,b):
    return(a*b)

# cikar fonksiyonu
def cikar(a,b):
    return(a-b)

#bol fonksiyonu
def bol(a,b):
    if(b==0): 
        return "Tanımsız"
    else:
        return(a/b)

a= int(input("1. sayıyı giriniz:"))
b= int(input("2. sayıyı giriniz:"))
print("Toplam sonucu:",topla(a,b))
print("Çıkarım sonucu:",cikar(a,b))
print("Çarpım sonucu:",carp(a,b))
print("Bölüm sonucu:",bol(a,b))


