def kvad(a,b,c):
    disk = pow(b,2)-4*a*c
    kva1 = (-b + pow(disk,(1/2)) ) / (2*a)
    kva2 = (-b - pow(disk,(1/2)) ) / (2*a)
    if (disk < 0 ):
        return print("diskriminant je záporný")
    elif(disk == 0):
        return kva1
    else:
        return [kva1, kva2]


print(kvad(1,3,1))