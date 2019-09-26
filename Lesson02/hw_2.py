thislist = [float(x) for x in input("Введите 2 числа: ").split()]
thislist.sort()
if thislist[1] % 1 > 0:
    thislist2 = list(range(int(thislist[0] // 1 + 1), int((thislist[1]+1))))
    print(thislist2)
else:
    thislist2 = list(range(int(thislist[0]//1 + 1), int((thislist[1]))))
    print(thislist2)