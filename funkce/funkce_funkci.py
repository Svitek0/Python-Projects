def secti(a,b):
    return a+b

def odecti(a,b):
    return a-b

def vynasob_soucet_a_rozdil(a,b,c,d):
    soucet = secti(a,b)
    rozdil = odecti(c,d)
    return soucet * rozdil

vysledek = vynasob_soucet_a_rozdil(1,2,5,3)
print("vysledek (a+b) * (a-b) = " + str(vysledek))