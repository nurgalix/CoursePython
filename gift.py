print("Программа - симулятор пирожка с сюрпризом")
import random
number = random.randint(1, 5)
if number == 1:
    print("\nПоздравляю вы выиграли - Футбольный мяч")
elif number == 2:
    print("\nПоздравляю вы выиграли - книгу про Историю")
elif number == 3:
    print("\nПоздравляю вы выиграли - immortal на Pudge")
elif number == 4:
    print("\nПоздравляю вы выиграли - носки")
else:
    print("\nПоздравляю вы выиграли - ничего")

input("\n\nPress Enter, to exit")
