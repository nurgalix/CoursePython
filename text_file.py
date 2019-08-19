#17.08.19
#Работа с текстовыми файлами
text = open("kek.txt", "w")

text.write("This boy has no chill!\n")
text.write("gege")
text.close()

text =  open("kek.txt", "r")
print(text.read())
text.close()
