"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""

file = open('file1.txt','w+')
file.write("Я гений и стараюсь учить питон")


file = open('file1.txt','r')
print(file.read(7))
file.close()