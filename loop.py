import random
word = "индекс"
low = -len(word)
high = len(word)
print("индекс")
for i in range(10):
    position = random.randrange(low, high)
    print(position, word[position])
input("\n\nPress Enter, to exit")
