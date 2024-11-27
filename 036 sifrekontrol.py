# Girilen bir şifre içinde,
# şifre en az 8 karakter olacaktır. 
# büyük harf, küçük harf, sembol(+,-,?,#,!,&,%,*), rakam var mı kontrol ediniz.
sifre= input("Şifre giriniz:")

mesaj=""
if (len(sifre)<8):
 mesaj="Şifre en az 8 karakter uzunluğunda olmalıdır \n"

semboller=['+','-','?','#','!','&','%','*','@']
buyukharfler=['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','W','X','Q']
kucukharfler=['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z','w','x','q']
rakamlar=['0','1','2','3','4','5','6','7','8','9']

sembolvar=False
buyukharfvar=False
kucukharfvar=False
rakamvar=False

# Döngü ile kontrol ediyoruz
for harf in sifre:
  if harf in semboller:
    sembolvar=True
  elif harf in buyukharfler:
    buyukharfvar=True
  elif harf in kucukharfler:
    kucukharfvar=True
  elif harf in rakamlar:
    rakamvar=True 

# Şimdi mantıksal şart kontrolü ile bakıyoruz ve uyarı mesajı oluşturuyoruz  
if (sembolvar==False):
 mesaj+="Şifrede sembol yok \n"

if (kucukharfvar==False):
 mesaj+="Şifrede küçük harf yok \n"

if (buyukharfvar==False):
 mesaj+="Şifrede büyük harf yok \n"

if (rakamvar==False):
 mesaj+="Şifrede rakam yok "
if (mesaj==""):
  print("Şifre kurallara uygun") 
else:
 print(mesaj)