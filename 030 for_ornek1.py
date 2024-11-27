# Aşağıdaki döngü 0'dan başlayıp 5'e kadar gider
# Sonuç: 0,1,2,3,4 olur
for i in range(5):
    print(i)

print("=== Başlangıç Bitiş ===")
# Aşağıdaki döngü 1'den 9'a kadar (9 dahil) ilerler
# range iki paramere alarak aralık sayabilir
for j in range(1,10):
    print(j)


print("=== Başlangıç, Bitiş, Artım ===")
# range 3 parametre alarak range(başlangıç,bitiş,artım) şeklinde sayabilir
# aşağıdaki sonuç 1,3,5,7,9 olur
for k in range(1,10,2):
    print(k)


print("==== Tek Sayılar ====")
for sayac in range(1,100,2):
    print(sayac)

print("=== Çift sayılar ===")
for say in range(0,100,2):
    print(say)