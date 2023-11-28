# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

num = int(input('Введите число: '))

first_num, second_num = 0, 1

index = 2
while second_num < num:
    first_num, second_num = second_num, first_num + second_num
    index += 1

if second_num == num:
    print(index)
else:
    print (-1)

