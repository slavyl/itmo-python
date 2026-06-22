from unittest import result

from matplotlib.pyplot import title

string1 = "Это строка."
string2 = "Это тоже строка."
result = string1 + string2

print("Результат конкатенации:")
print(result)

text = " Это ТЕСТОВАЯ строка дЛЯ теста ФУНкциЙ 123. "

print("Исходная строка:", text)
print("Длина строки:", len(text))
print("func title:", text.title())
print("func lower:", text.lower())
print("func upper:", text.upper())
print("func rstrip:", text.rstrip())
print("func lstrip:", text.lstrip())
print("func strip:", text.strip())
print("func strip('123. '):", text.strip('123. '))

param1 = "string" + str(15)
print(param1)

param2 = 15 + int("25")
print(param2)