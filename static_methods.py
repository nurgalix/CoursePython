#Классово верная зверюшка
#Демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1
#Основная часть
print("Нахожу значение атрибута класса Critter.total:", end=" ")
print(Critter.total)
print("\nСоздаю зверюшек")
crit1 = Critter("зверюшка 1")
crit2 = Critter("зверюшка 2")
crit3 = Critter("зверюшка 3")
Critter.status()
print("\nОбращаюсь к атрибуту класса через обьект:", end=" ")
print(crit1.total)
input()
