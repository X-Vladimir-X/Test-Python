# адача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть
import random

n = int(input('Брошено монет: '))
list = []
count = 0

for i in range(n):
    list.append(random.randint(0, 1))
    if list[i] == 0:
        count += 1
print(list)

heads = 0
tails = 0
for i in range(len(list)):
    if list[i] == 0:
        tails += 1
    else:
        heads += 1

if heads < tails:
    print(f'орлом упало {heads} штук')
elif heads > tails:
    print(f'решкой упало {tails} штук')
else:
    print(f'выпало одинаково {heads} {tails} штук')
