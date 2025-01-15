def harfNotuBul(x):
    harf=""
    if(0<x<40): 
        harf="F"   # if(x>0 and x<40): harf="F"
    elif(40<=x<55): 
        harf="D" 
    elif(55<=x<70): 
        harf="C"
    elif(70<=x<85): 
        harf="B"
    elif(85<=x<=100): 
        harf="A"
    else: 
        harf="Aralık dışı girildi"
    return harf
    
print(harfNotuBul(35)) # F yazar
print(harfNotuBul(55)) # C yazar
print(harfNotuBul(75)) # B yazar
print(harfNotuBul(90)) # A yazar

