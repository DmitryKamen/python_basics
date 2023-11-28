# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def rec(array, count, max_el):
    if count == 0:
        return array
    count -= 1
    if array[count] == max_el:
        array[count] = min(array)
    return rec(array, count, max_el)

array = [1, 3, 3, 3, 4]
print(rec(array, 5, max(array)))