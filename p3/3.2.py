import calendar
year = int(input("Введите год: "))
if calendar.isleap(year):
    print("Год високосный")
else:
    print("Год не високосный")

# year = int(input("Введите год: "))
#if year % 400 == 0:
#    print("Год високосный")
#elif year % 100 == 0:
#    print("Год не високосный")
#if year % 4 == 0:
#    print("Год високосный")
#else:
#    print("Год не високосный")

#8-16 стоки через конструкцию if-else с доп elif, а 1-6 через календарь