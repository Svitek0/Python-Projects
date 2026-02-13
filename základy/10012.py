promena = "Ahoj Karle, jak se máš?"

for i in range(len(promena)):
    print(promena[i])

for i in range(len(promena)):
    print(promena[-1-i])

for i in range(len(promena)-1, -1, -1):
    print(promena[i])

print("*************")

for i in range(len(promena)):
    print(promena[:i+1])

print("*************")

for i in range(len(promena)-2):
    print(promena[i:i+3])

print("*************")

#vipiste vždy vedle sebe prvni a posledni pismenko
#pak dtuhy a predposlední ... končíme v polivině textu

for i in range(int(len(promena)/2)+1):
    print(promena[i], promena[-i-1])


print("*************")
print(promena)
a = "   adsakosnd"
print(a.strip())

b = "4"
print(b.zfill(5))
