"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2
"""

def count_duble(arr):
    num = 0
    for i in set(arr):
        num += arr.count(i) //2
    return num
arr_1 = [1, 2, 3, 2, 3, 3, 3, 1]
print(count_duble(arr_1))

# второй вариант

arr = [1, 2, 3, 2, 3, 3, 3, 1]
num = 0
for i in set(arr):
        num += arr.count(i) //2
print(num)

# третий вариант

nums = [1, 2, 3, 2, 3, 3, 3]
my_set = set(nums)
res = []
for el in my_set:
    res.append(nums.count(el) // 2)


print(sum([nums.count(el) // 2 for el in set(nums)]))

# четвертый вариант

nums = [1, 2, 3, 2, 3, 3, 3]
my_set = set(nums)
res = []
for el in my_set:
    res.append(nums.count(el) // 2)

print(sum(res))


print(sum([nums.count(el) // 2 for el in set(nums)]))


count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            count += 1

print(count // 2)