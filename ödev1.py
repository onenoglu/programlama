print("İşletme Kar-Zarar Hesaplama")
x=int(input("FinansmanGelir:"))
y=int(input("PazarGelir:"))
z=int(input("KiraGelir:"))
gelir=x+y+z
print("Gelir:",gelir)
a=int(input("Ücret:"))
b=int(input("FinansmanGider:"))
c=int(input("PazarGider:"))
d=int(input("KiraGider:"))
e=int(input("MuhasebeGider:"))
gider=a+b+c+d+e
print("Gider:",gider)
kar=gelir-gider
if kar>1000:
    print("İşletme karlıdır.")
else:
    print("İşletme zarardadır.")
