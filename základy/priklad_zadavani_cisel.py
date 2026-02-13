from idlelib.configdialog import is_int

while(True):
    cislo_jako_text = input("zadej číslo: ")

    try:
        cislo = int(cislo_jako_text)
        break
    except:
        print("Musíte zadat číslo")

print("zadané číslo + 10 = " + str(cislo + 10))