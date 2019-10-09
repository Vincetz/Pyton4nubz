def calc(n):
    n = abs(n)
    res = 0
    while n > 0:
        n //= 10
        res += 1
    return res


if __name__ == '__main__':
    print('Калькулятор длинны целого числа.')
while True:
    try:
        n = int(input('Введите число: '))
        print(calc(n))
    except ValueError:
        print("Вы ввели не целое число, попробуйте еще раз!")
        continue
