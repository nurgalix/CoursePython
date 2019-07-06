#5.07.2019
#1 Пятикратный вывод имени
name = "Alman"
called = name * 5
print(called)
print(name)


#2.Создание троиных скобочек

print(
"""
sdasasopaasdokpasdkopasopaskopkop
"""
)


#3. Рантье

print(
"""
                      >>Рантье<<
     
   Программа расчитывает ваши расходы за месяц,введите суммы расходов по всем 
   статьям, так как вы богаты пишете суммы только в долларах.
"""
)
food = int(input("На еду и рестораны: "))
car = int(input("Технические обслуживание машины: "))
rent = int(input("Квартплата: "))
fun = int(input("Развлечение: "))
air = int(input("Аренда самолёта: "))
total = food + car + rent + fun + air
print("\nВаши расходы в месяц ровно:" , total)


#4. Сколько вам секунд
print("\n\n\n")
seconds = int(input("Здравствуйте, сколько вам лет?"))
print("\nТвой нынешний возвраст - свыше", seconds * 365 * 24 * 60 * 60, "секунд")



#5. Невиданное блюдо

food1 = input("Напишите свое любимое блюдо: ")
food2 = input("Напишите свое второе любимое блюдо: ")
dword = food1 + food2
print("Любимая еда Ленина:", dword.capitalize())



#6. Щедрый посититель
total = int(input("Оплатите счет:"))
print(total * 15 / 100, total * 20 / 100)




#7. Автодиллер

value = int(input("Ввести стоимость автомобиля:"))
tax = 500
reg_fee = 600
agent = 740
delivery = 200
print("Окончательная цена автомобиля, с учётом агентских сборов и доставки:", agent + delivery + value)
