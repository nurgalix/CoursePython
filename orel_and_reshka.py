#7.07.19   Орёл и Решка
import random
orel = 0
reshka = 0
#Написав перед переменной global, можно переменную не инициализировать
upper = 1
while upper < 101:
    random_num = random.randint(1, 2)
    if random_num == 1:
        orel += 1
    else:
        reshka += 1
    upper += 1
print("Это программа подбросило монету 100 раз в итоге", orel, " раз выпало Орёл и", reshka, "раз Решка")
