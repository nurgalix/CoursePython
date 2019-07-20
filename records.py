#Records 16.07.19
#Демонстрирует списочные методы
scores = []
choice = None
while choice != "0":
    print(
    """

    0 - exit
    1 - show record
    2 - add record
    3 - delete records
    4 - sort(irovat') record
    """
    )
    choice = input("Ваш выбор: ")
    print()
    #выход
    if choice == "0":
        print("До свидание.")
    #вывод лучших результатов на экран
    elif choice == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    #Добавление рекорда
    elif choice == "2":
        score = int(input("Впишите свой рекорд: "))
        scores.append(score)
    #Удаление рекорда
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?:"))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержится в списке рекордов.")
    #сортировка рекордов
    elif choice == "4":
        scores.sort(reverse = True)
    #непонятный пользывательский вывод
    else:
        print("Извините в меню нет пункта", choice)
input("\n\n")
        
