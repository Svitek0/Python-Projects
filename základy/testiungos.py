vstup = input("zadejte číslo : ")
try:
    cislo = int(vstup)
except:
    cislo = 0

if(cislo > 10):
    print("číslo je větší než 10")
if(10<cislo<20):
    print("vaše číslo je menší než 20 ale větší než 10")

if((cislo%2) == 0):
    print("číslo je sudé")
else:
    print("číslo je liché")

