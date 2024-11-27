# aşağıdaki döngü 10'dan 0'a kadar(0 dahil değil) birer birer azaltarak sayacaktır
# 10,9,8,7,6,5,4,3,2,1 sonucu yazılacaktır
for i in range(10,0,-1):
    print(i)


# 10,8,6,4,2,0 şeklinde yazmasını istiyorsak
print("=== İkişer geriye say ===")
for j in range(10,-1,-2):
    print(j)