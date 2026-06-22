
full_name = input("Введите свое имя и фамилию:\n")

full_name = full_name.title()

first_name, last_name = full_name.split()

login = last_name[:4] + first_name[0]

print(f" {last_name} {first_name}: {login}")