#7.07.2019
#Отгадай число
print("\tДобро пожаловать в игру 'Отгадай число'")
print("Я загадал натуральное число из диапазона от 1 до 100")
print("Постарайтесь отгадать число за минимальное количество попыток, Удачи!\n")
import random
random_num = random.randint(1, 100)
num = int(input("Введите число: "))
tries = 1 
while random_num != num:
    if random_num > num:
        print("Больше...")
    else:
        print("Меньше...")
    num = int(input("Ваше предположение: "))
    tries += 1

print("\nВам удалось отгадать число! Это  в самом деле", random_num)
print("Вы затратили на отгадование всего лишь ", tries, " попыток!\n")
input("\n\nPress Enter, to exit")
