# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#  не превосходящие числа N.

# p = int(input("Показатель степени: "))
# n = int(input("Предел: "))

# i = 1
# while i ** p <= n:
#     print(i ** p, end=' ')
#     i += 1

# print("\nПоследнее число,"
#       " возведенное в степень:", i - 1)


n = int(input("Введите число: "))
i = 0
power = 1
power_prev = 1

print("Ряд целых степеней двойки  этого числа: ")

while power <= n:
    power_prev = power
    power = 2 ** (i + 1)

    i += 1

    print(f'{power_prev}', end=' ')
