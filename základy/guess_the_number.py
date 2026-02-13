from random import randint

import numpy as np

cislo = np.random.randint(1,21)
print(cislo)
pocet = 0

while(True):
    pokus = input("zadejte číslo od 1 do 20 : ")
    pocet +=1
    try:
        pokusINT = int(pokus)
        if (pokusINT == cislo):
            print("Správně!")
            print("Počet pokusů :" + str(pocet))
            break
        elif (pokusINT > cislo):
            print("Hledané číslo je MENŠÍ.")
        elif (pokusINT < cislo):
            print("Hledané číslo je VĚTŠÍ.")
    except:
        print("Musíte zadat číslo")

