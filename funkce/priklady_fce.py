def druhy_nejvetsi(vlist):
    if vlist[0]> vlist[1]:
        max = vlist[0]
        druh = vlist[1]
    else:
        max = vlist[1]
        druh = vlist[0]
    for i in range(len(vlist)):
        if(vlist[i] > max):
            druh = max
            max = vlist[i]
        if(vlist[i]>druh and vlist[i] < max):
             druh = vlist[i]

    return druh


a = [10,2,5,40,30,12,20,34,-9,0,1]
x = druhy_nejvetsi(a)
print(x)




def je_prvocislo(a):
    if a <2:
        return False

    for i in range(2,a):
        if a%i==0:
            return False

    return True

cislo = 21
print(je_prvocislo(cislo))
