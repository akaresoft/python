# Girilen iki sayı arasında 3'e bölünen kaç sayı olduğunu bulunuz

def aralikSay(a,b):
    sayac=0
    for i in range(a,b+1):
        if(i%3==0):
            sayac+=1
            print("Üçe bölünen sayı:",i)
    return sayac

# aşağıdaki şekilde fonksiyonu çağırırsak 1 ile 10 arasında 
# 3,6,9 şeklinde 3 sayı bulur ve ekrana 3 yazar.
print(aralikSay(1,10))

