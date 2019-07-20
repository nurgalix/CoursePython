#19.07.19
import random
WORDS = ["beautiful", "papi4", "coach", "control", "forward", "reason", "lose"]
for _ in range(len(WORDS)):
    word = random.choice(WORDS)
    WORDS.remove(word)
    print(word, end = " ")
    







"""
new = []

while new != WORDS:
    if word not in new:
        print(word)
        new.append(word)
    else:
        print("1")


input("\n\n")
#loh = WORDS.remove(WORDS[1])
#print(loh)
#print(WORDS)
#ЕСЛИ в Списке new не будет рандомное слово word то выводит на экран и после этого
#добавить это значение в список

"""
