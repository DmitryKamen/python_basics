# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

# m = 0
# n = len(list_1)
# near = 0
# flag = True
# while (m < max(list_1) and flag):
#     for i in range(n):
#         if list_1[i] + m == k or list_1[i] - m == k:
#             near = list_1[i]
#             flag = False
#     m += 1
# print(near) 
# не совсем верное решение

# buf = 0
# n = len(list_1)
# for i in range(n):
#     if buf <= k and list_1[i] > buf or buf >= k and list_1[i] < buf and list_1[i] > k:
#         buf = list_1[i]
        
# print(buf)  
# # верное решение но не есть лучшее

# - решение в одну строчку
# print(min(list_1,key=lambda x: abs(x-k)))

# - решение через модуль
#  создаем новый список
list_2 = []
# находим можуль от k до каждого элемента списка
for i in list_1:
    list_2.append(abs(k-i))
# Находим минимальный модуль
mn = list_2[0]
for i in list_2:
    if(mn > i):
        mn = i
# Узнаем индекс минимального модуля
index = list_2.index(mn)
print(list_1[index])




