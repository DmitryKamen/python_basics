# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# var1 = '5 5'
# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'

var1 = '1 4'
var2 = '1'
var3 = '3 4 5 6'


import re
n1 = re.findall(r'\d+', var2)
list1 = []
for i in n1:
    list1.append(int(i))
# print(list1)
# var2.split()  # or .split(" ")
# var3.split()  # or .split(" ")
n2 = re.findall(r'\d+', var3)
list2 = []
for i in n2:
    list2.append(int(i))
# print(list2)

general = set()
m1 = set(list1)
# m1.remove(' ')
m2 = set(list2)
# m2.remove(' ')
general = m1.union(m2) - m1.difference(m2) - m2.difference(m1)
gen = list(general)
temp = 0
for i in range(len(gen)):
    indexMin = i
    for j in range(len(gen)):
        if gen[j] > gen[indexMin]:
            indexMin = j
        if gen[indexMin] == gen[i]:
            continue
        temp = gen[i]
        gen[i] = gen[indexMin]
        gen[indexMin] = temp
        j += 1
    i += 1
print(*gen)  