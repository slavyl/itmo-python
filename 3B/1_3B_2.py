import names

all_names = []
group_am = []
group_nz = []

for _ in range(100):
    all_names.append(names.get_first_name())

for name in all_names:
    if "A" <= name[0].upper() <= "M":
        group_am.append(name)
    else:
        group_nz.append(name)

print("Все сгенерированные имена:\n")

print("\nИмена A-M:")
for i, name in enumerate(group_am, start=1):
        print(f"{i:2}. {name}")

print("\nОстальные имена:\n")
for i, name in enumerate(group_nz, start=1):
    print(f"{i:2}. {name}")