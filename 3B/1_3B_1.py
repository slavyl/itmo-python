from random import randint

numbers = []
result = []

threshold = 50

for _ in range(20):
    numbers.append(randint(1, 100))

for number in numbers:
    if number > threshold:
        result.append("High")
    else:
        result.append("Low")

print(f"Пороговое значение: {threshold}\n")

for number, status in zip(numbers, result):
    print(f"{number:3} -> {status}")