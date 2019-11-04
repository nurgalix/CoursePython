try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число!")
    print(e)
