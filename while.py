#6.07.2019
#Кости, демонстратирует генерацию случайных чисел
import random
#Создаем случайные числа из диапазона 1-6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2
print("При вашем броске выпало", die1, "и", die2, "Очков в сумме", total)
input()
 
"""
Nurgali
"""
