thislist = [float(x) for x in input("Введите 2 числа: ").split()]
thislist.sort()
if thislist[-1] % 1 > 0:
    thislist[-1] = thislist[-1]+1
thislist2 = list(range(int(thislist[0]), int(thislist[1])))
pos = []
for x in thislist2:
    if x > 0:
        pos.append(x)
        continue
print(pos)
    
    #Код написан в кооперации с Варбанцом
