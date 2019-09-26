import random
N = random.randint(10, 20)
while N > 0:
    pl1 = int(input("Игрок 1, введите количество забераемых спичек от 1-3: "))
    while not int(pl1) in range(1, 4):
        pl1 = int(input("Некорректное число! Бери от 1-3 спичек:"))
    N = N - pl1
    if N <= 0:
        print("Проиграл Игрок 1")
        break
    pl2 = int(input("Игрок 2, введите количество забераемых спичек от 1-3: "))
    while not int(pl2) in range(1, 4):
        pl2 = int(input("Некорректное число! Бери от 1-3 спичек:"))
    N = N - pl2
    if N <= 0:
        print("Проиграл Игрок 2")
        break
print("Game Over")
