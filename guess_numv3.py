#8.07.19 Считалка
#Демонстрирует использование функции range()
print("Посчитаем:")
for i in range(10):
    print(i, end=" ")
print("\n\nПеречислим кратные пяти:")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\n\nПосчитаем в обратном порядке:")
for i in range(10, 0, -1):
    print(i, end=" ")

reiteration = 0
word = input("\n\nНапишите слово")
for letter in word:
    reiteration += 1
    print(letter, " ", reiteration)



#Анализатор текста
#Демонстрирует работу функции  len() и оператора in
message = input("Введите текст: ")
print("\nДлина введенного текста составляет", len(message))
print("\nСамая частая согласная , 'т'.")
if "т" in message:
    print("встречается в вашем тексте.")
else:
    print("не встречается в вашем тексте.")
input("\n\nPress Enter, to exit")


"""
import random

number = random.randint(1, 100)

while True:
    print("Is it your number", number)
    char = input("Yes or No: ")
    if char == "Yes":
        break
    else:
        char = input("Is it less(<) or more(>): ")
        if char == "<":
"""
