#Игра Анаграммы 12.07.19
import random
WORDS = ("пайтон", "дота", "чинчопа", "дединсайд", "мал", "телеграм", "токач", "папич", "папаня")
word = random.choice(WORDS)
jumble = ""
correct = word
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("Здравствуйте это игра Анаграммы")
print("Вот анаграмма", jumble)
guess = input("Попробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожелею вы ошиблись, попробуйте заново")
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == correct:
    print("\nПоздравляю вы выиграли!!!")
print("Спасибо за игру.")
input("\n\nPress Enter, to exit")

