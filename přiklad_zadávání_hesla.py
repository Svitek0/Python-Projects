while(True):
    heslo = input("zadejte heslo: ")

    skutecne_heslo = "heslo123"

    if (heslo == skutecne_heslo):
        print("správné heslo! ")
        break
    else:  print("špatné heslo. zadej znovu")
