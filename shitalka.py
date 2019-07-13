#12.07.19 Shitalka
i = int(input("Введите начало счета: "))
j = int(input("Введитк конец счета: "))
k = int(input("Введите интервал: "))
for start in range(i, j + 1, k):
    print(start, end=" ")
input("\n\nPress Enter, to exit")
