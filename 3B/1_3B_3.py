letters = []

while True:
    word = input("Введите слово: ")

    if word == "":
        break

    letters.append(word[0])

result = "".join(letters)

print("Акростих:", result)