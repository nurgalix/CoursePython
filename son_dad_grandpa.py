#19.07.19

choice = None
common = {"Nurgali" : "Sharapat"}
newcommon = {"Nurgali" : "Nuraly"}
while choice != "0":
    print(
    """
    "Кто твой папа"
    
    Меню
    0 - Выйти
    1 - Найти отца человека / Введите имя человека, а программа скажет его отца
    2 - Добавить пару / 
    3 - Изменить пару / Если пара не правильная, то можно изменить 
    4 - Удалить пару
    5 - Найти деда
    6 - Добавить внука и деда
    7 - Удалить внука и деда
    """
    )
    choice = input("Ваш выбор: ")
    
    # выход
    if choice == "0":
        print("До свидание.", end = "")
    elif choice == "1":
        son = input("Имя сына: ")
        if son in common:
            father = common[son]
            print("\n", son, " ребенок ", father, sep = "")
        else:
           print("\nУвы, этот ребенок мне незнаком.")
    elif choice == "2":
        son = input("Какого человека хотите добавить: ")
        if son not in common:
            father = input("Напишите отца этого человека: ")
            common[son] = father
            print("\n", son, " Добавлен в словарь", sep = "")
        else:
            print("\nТакой человек уже есть! Попробуйте изменить его в меню.")
    elif choice == "3":
        son = input("Какому человеку хотите изменить отца: ")
        if son in common:
            father = input("Впишите отца этого человека: ")
            common[son] = father
            print("\nЧеловек", son,"был переопределен.")
        else:
            print("\nТакого человека нет в словаре.")
    elif choice == "4":
        son = input("Какое значение хотите удалить: ")
        if son in common:
            del common[son]
            print("Человек", son , "удален.")
        else:
            print("\nНичем не могу помочь, человек", son, "нет в словаре.")
    elif choice == "5":
        grandson = input("Введите имя человека: ")
        if grandson in newcommon:
            grandpa = newcommon[grandson]
            print("\n", grandson, " внук ", grandpa, sep="")
        else:
            print("\nУвы, этот ребенок мне незнаком.")
    elif choice == "6":
        grandson = input("Напишите имя внука: ")
        if grandson not in newcommon:
            grandpa = input("Напшите имя дедушки: ")
            newcommon[grandson] = grandpa
            print("\n", grandson," и ", grandpa," добавлен в словарь", sep = "")
        else:
            print("\nТакой внук уже есть! Попробуйте изменить его в меню.")
    elif choice == "7":
        grandson = input("Введите имя внука, который хотите удалить из списка: ")
        if grandson in newcommon:
            del newcommon[grandson]
            print("Пара", grandson, " и ", grandpa, " были удалены из словаря", sep="")
        else:
            print("\nНичем не могу помочь, внук", grandson, "нет в словаре.")
    else:
        print("\nИзвините, в меню нет пункта.", choice)
input("\n")
print(common)
