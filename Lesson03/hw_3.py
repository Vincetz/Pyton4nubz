def rect(a, b):
    if a < 0 and b < 0:
        a *= -1
        b *= -1
    elif a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    return a * b


def triangle(a, b, c):
    if a < 0 and b < 0 and c < 0:
        a *= -1
        b *= -1
        c *= -1
    elif a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    elif c < 0:
        c *= -1
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def circle(r):
    if r < 0:
        r *= -1
    return 3.14159 * r**2

if name == 'main':
    print("Калькулятор площади фигур.\n"
      "Введите 1 для Прямаугольника; 2 для Триугольника ; 3 для Круга ; 4 для выхода")

while True:
    try:
        choice = int(input("Укажите номер действия: "))
        if choice == 1:
            x, y = [float(x) for x in input("Укажите 2 стороны прямоугольника через пробел: ").split()]
            print("Площадь вашего прямоугольника равна: ", rect(x, y))
            continue
        elif choice == 2:
            x, y, z = [float(x) for x in input("Укажите 3 стороны триугольника через пробел: ").split()]
            print("Площадь вашего триугольника равна: ", triangle(x, y, z))
            continue
        elif choice == 3:
            r = float(input("Укажите радиус круга: "))
            print("Площадь вашего круга рана: ", circle(r))
            continue
        elif choice == 4:
            print("Окончание программы!")
            break
        else:
            print("Вы указали неверную команду, попробуйте еще раз!")
            continue
    except ValueError:
        print("Вы ввели некоректное значение, попробуйте еще раз!")
# Программа может принимать отрицательные значения, это предусмотрена как ошибка ввода пользователя(Защита от дурака. Длина не может быть отрицательной).
