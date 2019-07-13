import random
WORDS = ("пайтоннеговно",
         "превысокомногорассмотрительствующий",
         "тысячадевятьсотвосьмидесятидевятимиллиметровый",
         "водогрязеторфопарафинолечение",
         "человеконенавистничество",
         "папич")
word = random.choice(WORDS)
jumble = ""
correct = word
attempt = 1
temp = 0
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("Здравствуйте это игра Анаграммы, вам дается 5 попыток для отгадование исходного слово")
print("Вот анаграмма >>>>   ", jumble)
print("Если хотите воспользоваться подсказкой, напишите символ '!'")
guess = input("Попробуйте отгадать исходное слово:")
while guess != correct and guess != "":
    if guess == "!":
        print("Первая буква", correct[0])
        temp += 1
    if guess != correct and guess != "":
        print("К сожелею вы ошиблись, попробуйте заново")
    guess = input("Попробуйте отгадать исходное слово: ")
    attempt += 1
    if guess == correct:
        continue
    if attempt == 5:
        print("К сожелению вы проиграли :(")
        break
if guess == correct:
    if temp == 0 and attempt == 1:
        print("ПРЕВОСХОДНО ВЫ ВЫИГРАЛИ, ВАМ НАЧИСЛЯЕТСЯ 10000000000 баллов")
    elif temp > 0:
        print("Поздравляю вы справились, но использывали подсказку :/ , поэтому вам начисляется 50 баллов")
    else:
        print("Поздравляю вы выиграли, вам начисляется 100 баллов")
input("\n\nPress Enter, to exit")
