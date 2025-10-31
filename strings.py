text = "ah'oj"
text2 = 'aahoj'
text3 = 'aaaaaaaahoj \'asd\'dsada'
text4 = "soubor je na C:\\ProgramFiles\\Adobe..."
text5 = "text 1 (\\(\\n))\n text 2"

print(text4)
print(text5)

a = "abc"
b = "def"
print(a + b )

c = "a"
for i in range(5):
    c = c + "a"

print(c)


promena = "ahoj Karle, jak se máš?"

print(promena[6])  # indexopbvaní od nuly !!!

print(len(promena))

for i in range(len(promena)):
    print(promena[i])

print("*** \n")
print(promena[len(promena)-1])
print(promena[-1])


print(promena[5:10:2])  # znaky od <a;b) !!!  včetně a  !!!
print(promena[10:5:-2])

print (promena[5:])  # včetně 5
print (promena[:5])

print (promena[::-1])  # string pospátku

print(promena)