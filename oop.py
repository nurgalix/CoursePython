#Зверюшка с атрибутами
#Демонстрирует метод-конструктор
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет зверюшка!")
    def talk(self):
        print("\nПривет, Я зверюшка - экзепляр класса Critter.")
#основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input()
