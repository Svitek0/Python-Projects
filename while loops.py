# for i in range(11):
#     if((i%2)==0):
#         print(i, "číslo je sudé")
#     else:
#         print(i,  "čislo je liché")
#
# a = 0
#
# while (a==0):
#     x = input("napiš číslo : ")
#     try:
#         a = int(x)
#     except:
#         a = 0

# while (True):
#     x = input("y / n : ")
#     if (x == "y"):
#         while (True):
#             x = input("napiš číslo : ")
#             try:
#                 a = int(x)
#             except:
#                 a = 0
#             if (a == 5):
#                 print("uhodl jsi číslo")
#                 break
#     else:
#         break
#     y = input("chcete začít znovu ? (y/n)")
#     if y == "n":
#         break

a = 0
while (True):
    x = input("napiš číslo : ")
    try:
        a = int(x)
        break
    except:
        pass
    print(a)
