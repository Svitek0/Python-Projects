import random
from traceback import print_tb

x= random.randint(10,20)

def hod_k6():
    """
    simuluje hod kostkou
    :return:
    int: rand <1;6>
    """
    hod = random.randint(1, 6)
    return  hod

print(hod_k6())
print("*******************")

def pocet_hodu1():
    pocet = 0
    while (True):
        pocet+=1
        hod = hod_k6()
        if(hod == 6):
            break
    return pocet

print(pocet_hodu1())

def hazeni_n_krat(n):
    cetnost = [0]*20
    for i in range(n):
        x = pocet_hodu1()
        if x > 20:
            x= 20
        cetnost[x-1] += 1

    return cetnost

random.seed(5)
print(hazeni_n_krat(10000))



