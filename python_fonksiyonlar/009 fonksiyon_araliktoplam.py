# verilen iki sayı arasındaki sayıların toplamını bulan fonksiyon yazınız
def aralikTopla(x,y):
    toplam=0
    for i in range(x,y+1):
        toplam+=i
    return toplam


#a=int(input("1. sayıyı giriniz:"))
#b=int(input("2. sayıyı giriniz:"))
#print("Toplam sonucu:",aralikTopla(a,b))   
# 100 ile 200 arasındaki sayıları toplarsak
toplam1=aralikTopla(100,200)
toplam2=aralikTopla(50,100)
print("Çıkarımı =",toplam1-toplam2)


