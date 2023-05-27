# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input('Введите число:  '))

suma = 0
mult = 1

while n > 0 and n < 1000:
    digit = n % 10
    if digit != 0:
        suma = suma + digit
        mult = mult * digit
        n = n // 10

print(suma)
