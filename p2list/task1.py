list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]

print("Исходный список:", list1)

list1[0] = 100
list1[3] = 55
print("После изменения элементов:", list1)

list1.append(999)
print("После append:", list1)

list1.insert(2, 777)
print("После insert:", list1)

removed_item = list1.pop(4)
print("Удаленный элемент:", removed_item)
print("После удаления по позиции:", list1)

last_item = list1.pop()
print("Удаленный последний элемент:", last_item)
print("После удаления последнего элемента:", list1)

list1.sort(reverse=True)
print("Сортировка по убыванию:", list1)

list2 = [3, 5, 6, 2, 33, 6, 11]

sorted_list = sorted(list2)

print("Исходный list2:", list2)
print("Отсортированный sorted_list:", sorted_list)