# 18. *Реализуйте алгоритм перемешивания списка.

from random import Random, randint

num = int(input('Введите число '))
list = []
for i in range(num):
    list.append(randint(-num, num+1))
print(list)

list2 = list[:]
list_length = len(list2)  # возвращает количество элементов объекта
for i in range(list_length):
        index = randint(0, list_length - 1)
        temp = list2[i]
        list2[i] = list2[index]
        list2[index] = temp
print(list2)