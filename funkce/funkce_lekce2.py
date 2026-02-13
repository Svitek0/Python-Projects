def secti(a,b):
    globalni_promena=20
    vysledek = a+b+globalni_promena
    return [vysledek, globalni_promena]

def secti_tuple(a,b):
    globalni_promena=20
    vysledek = a+b+globalni_promena
    return (vysledek, globalni_promena)

globalni_promena = 10

x = secti(8,1)
print(x)
print(type(x))

z = secti_tuple(3,3)
print(z)
print(type(z))
