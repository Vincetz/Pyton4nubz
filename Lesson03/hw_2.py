def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

if __name__ == '__main__':
    while True:
        try:
            x, y = [int(x) for x in input("Укажите 2 числа: ").split()]
            if x < 0 and y < 0:
                x *= -1
                y *= -1
                print('НОК этих чисел:', nok(x, y))
            elif x < 0:
                x *= -1
                print('НОК этих чисел:', nok(x, y))
            elif y < 0:
                y *= -1
                print('НОК этих чисел:', nok(x, y))
            else:
                print('НОК этих чисел:', nok(x, y))
        except ValueError:
            print("Введение дробных или символьных значений не возможно!\n"
                  "Введите 2 целых числа через пробел!")
            continue
