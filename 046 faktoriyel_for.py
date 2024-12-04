
n= int(input("Faktöriyeli alınacak sayıyı giriniz:"))
if (n==0):
    print("0!=1 olur")
elif(n>=1):
    fakt=1
    for i in range(1,n+1):
        print(i)
        fakt=fakt*i

    print("Faktöriyel sonucu:",fakt)