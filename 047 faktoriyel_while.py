
n= int(input("Faktöriyeli alınacak sayıyı giriniz:"))
if (n==0):
    print("0!=1 olur")
elif(n>=1):
    fakt=1
    i=1
    while(i<=n):
        #print(i)
        fakt=fakt*i
        i=i+1 # i+=1

    print("Faktöriyel sonucu:",fakt)