#Просто зверюшка
#Демонстрирует  простейщие класс и объект
class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")
#Основная часть
crit = Critter()
crit.talk()
input("\n\nPress Enter")
