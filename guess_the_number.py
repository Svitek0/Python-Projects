from random import randint

import numpy as np

cislo = np.random.randint(1,21)
print(cislo)

while(True):
    pokus = input("zadejte číslo od 1 do 20 : ")

    try:
        pokusINT = int(pokus)
        if (pokusINT == cislo):
            print("Správně!")
            break
        elif (pokusINT > cislo):
            print("Hledané číslo je MENŠÍ.")
        elif (pokusINT < cislo):
            print("Hledané číslo je VĚTŠÍ.")
    except:
        print("Musíte zadat číslo")

