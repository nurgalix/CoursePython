#17.07.19 рекорды_v2
#Демонмтрирует вложенные последовательности
scores = []
choice = None
while choice != "0":
    print(
        """
        0 - Выйти из программы
        1 - Показать рекорды топ5
        2 - Добавить рекорды
        """
        )
    choice = input("Ваш выбор:\n")
    if choice == "0":
        print("До свидание")
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = input("Впишите его результат: ")
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #В списке остается только пять рекордсменов
    else:
        print("Извините, в меню нет такого пункта", choice)

input("\n\n")







#Распределенные ссылки
print("\n\n\n\n\n\n\n")
mike = ["белая рубашка", "комбинизон", "пиджак"]
mr_dawson = mike
honey = mike
print(mike)
print(mr_dawson)
print(honey)


print("\n\n\n\n\n")
honey[2] = "красный свитер"
print(honey)
print(mike)
print(mr_dawson)

"""
mike = ["белая ркбашка", "комбинизон", "пиджак"]
honey = mike[:]
honey[2] = "красный свитер"
print(honey)
print(mike)
"""
