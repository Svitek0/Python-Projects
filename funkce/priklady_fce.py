def druhynejvetsi(list):
    max = 0
    druh=0
    for i in range(len(list)):
        if(list[i] > max):
            druh = max
            max = list[i]
        if(list[i]>druh and list[i] < max):
             druh = list[i]

    return druh


a = [10,2,5,40,30,12,20,34]
x = druhynejvetsi(a)
print(x)
