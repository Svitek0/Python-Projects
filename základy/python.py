vstup = input("zadejte číslo : ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

if(cislo < 10):
    print("vaše číslo je menší než 10")
elif(10 < cislo <20):
    print("vaše číslo je menší než 20 ale větší než 10")
elif(cislo > 20):
    print("vaše číslo je větší než 20")