name = input("Привет, как тебе зовут? ")
age = input("Сколько тебе лет? ")
weight = int(input("И последний вопрос сколько ты весишь? "))
print("Привет", name, "Я сейчас скажу несколько бесполезных фактов")
print("\nTы родился примерно", 2019 - int(age))
moon_weight =  weight / 6
sun_weight = weight * 27.1
print("Знаете ли вы, что на Луне вы висели бы всего", moon_weight, "кг")
print("А вот находясь в солнце, вы весели", sun_weight, "кг.   Да-да но увы это продалжалось бы не так долго")
print("\a")
input("\n\nPress Enter, chtoby vyiti.")
