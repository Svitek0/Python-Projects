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

for i in range(len(promena)-1):
    print(promena[i:2])

