def odpocet(n):
    if n == 0:
        print("BOOM")
        return
    else:
        print("Odpocet "+str(n))
        (odpocet(n-1))

odpocet(10)
