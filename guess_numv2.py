#Отгадай число v.2
print("\tДобро пожаловать в игру 'Отгадай число'v2")
print("Я загадал натуральное число из диапазона от 1 до 100")
print("Постарайтесь отгадать число за 10 попыток, Удачи!\n")
import random
random_num = random.randint(1, 100)
num = 0
tries = 1
attempt = 1
while random_num != num:
    num = int(input("Ваше предположение: "))
    if random_num == num:
        print("\nВам удалось отгадать число! Это  в самом деле", random_num)
        print("Вы затратили на отгадование всего лишь ", tries, " попыток!\n")
        continue
    if random_num > num:
        print("Больше...")
    else:
        print("Меньше...")
    if attempt == 6:
        print("You are Loserrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        break
    attempt += 1
    tries += 1
input("\n\nPress Enter, to exit")


