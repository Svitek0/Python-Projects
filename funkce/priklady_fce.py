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


def prvocisla_seznam(vList):
    prvocisla = 0
    for i in range(len(vList)):
        if je_prvocislo(vList[i]):
            prvocisla+=1
    return prvocisla

cislo = [5,13,7,3,11]
print(prvocisla_seznam(cislo))


def adding(a,b):
    return a+b

def subtracting(a,b):
    return a-b

def calculate(function, a,b):
    return function(a,b)

print("**************")
print(calculate(adding,1,2))
print(calculate(subtracting,1,2))

inp1 = int(input("Zadej číslo : "))
inp2 = int(input("zadej truhy cislo : "))
inp3 = input("zadejte funkci (+/-)")

if inp3 == "+":
    print(calculate(adding,inp1,inp2))
elif inp3 =="-":
    print(calculate(subtracting, inp1, inp2))
else:
    print("neznámá funkce")


def jina_fce(a,b,c=10,d=10):
    return a+b+c+d

print(jina_fce(1,2,5,5))

def jeste_jina_fce(*args):
    soucet =0
    for i in range(len(args)):
        soucet+=args[i]
    return soucet

print(jeste_jina_fce(1,2,55,1,4,8))