# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input("Введите количество учащихся в первом классе: "))
# b = int(input("Введите количество учащихся во втором классе: "))
# c = int(input("Введите количество учащихся в третьем классе: "))

# result = 0
# for i in a, b, c:
#     result += i // 2 + i % 2

# print(result)

# print((a % 2 + a // 2) + (b % 2 + b // 2) + (c % 2 + c // 2))

from math import ceil

n1 = int(input("Введите количество учеников в первом классе "))
n2 = int(input("Введите количество учеников во втором классе "))
n3 = int(input("Введите количество учеников в третьем классе "))

print (ceil(n1 / 2) + ceil(n2 / 2) + ceil(n3 / 2))