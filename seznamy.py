promena = [1, 2, 3, 4, 5]

print(promena)

p2 = [1, "abc", 5.5, True, [1,2,"dsa"]]
print(p2)
print(p2[2])
print(type(p2[4][1]))

p2 = [1, "abc", 5.5, True, [1,2,"dsa"]]
print(p2)
print(p2[1][1])
print(type(p2[4][1]))

p2 = [1, "abc", 5.5, True, [1,2,"dsa"]]
print(p2)
print(p2[:3])

x = [1, 2, 8, 4, 6, 11, 7, 4]

for i in range(len(x)):
    if (i%2): print(x[i])

for i in range(len(x)):
    if (i % 2) ==0:
        print(x[i])
