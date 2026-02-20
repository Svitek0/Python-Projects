def kvad(a,b,c):
    disk = pow(b,2)-4*a*c
    kva1 = (-b + pow(disk,(1/2)) ) / (2*a)
    kva2 = (-b - pow(disk,(1/2)) ) / (2*a)
    if (disk < 0 ):
        return [] #print("diskriminant je záporný")
    elif(disk == 0):
        return kva1
    else:
        return [kva1, kva2]

def kvadratic_test():
    results=[]
    for i in range(5):
        results.append(kvad(1,i,1))
    return results

vysledky = kvadratic_test()
for vysledek in vysledky:
    print(vysledek)
