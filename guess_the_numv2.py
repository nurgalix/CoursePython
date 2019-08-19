#15.08.2019
#Отгадай число
#С функций
import random
def ask_number(low, high, step = 1):
    response  = None
    while response not in range(low, high):
        response = int(input("Введите число: "))
        num = response
    return response
print("\tДобро пожаловать в игру 'Отгадай число'")
print("Я загадал натуральное число из диапазона от 1 до 100")
print("Постарайтесь отгадать число за минимальное количество попыток, Удачи!\n")
random_num = random.randint(1, 100)
def main():
    guess = ask_number(1, 100)
    tries = 1
    while random_num != guess:
        if random_num > guess:
            print("Больше...")
        else:
            print("Меньше...")
        guess = ask_number(1, 100)
        tries += 1
    print("\nВам удалось отгадать число! Это  в самом деле", random_num)
    print("Вы затратили на отгадование всего лишь ", tries, " попыток!\n")

main()
input("\n\nPress Enter, to exit")

