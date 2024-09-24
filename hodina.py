#Teória:
    #for i in range(0, 100):             #zopakuje sa 100x a hodnota premennej i sa zvyšuje

    #for i in range(0, 100, 2):          # tá 2 sa volá step a o toľko sa zvyšuje premenná i

    #Ulohy:
#def shredr():
#    for i in range(1000, 10000):
#        lastwodigits = i % 100
#        firstwodigits = i // 100
#        if firstwodigits ** 2 + lastwodigits ** 2 == i:
#            print (i)


#def shreder2():
#    tog = 0
#    for i in range(1000, 10000):
#        tog += i           # tog += i
#    return tog

#print(shreder2())


def faktorial():
    a = int(input("Zadaj a:"))
    b = a + 1
    tog = 1
    for i in range(1, b):
        tog = tog * i           # tog += i
    return tog

print(faktorial())