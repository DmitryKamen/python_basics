# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# 700

# print('Введите колитчество километров проезжает машина в день: ')
# n = int(input())
# print('Введите количество километров, которое необходимо проехать: ')
# m = int(input())
# print(f'Чтобы проехать нужное количество километров необходимо {int((m + n - 1) / n)}')

n = int(input("Введите сколько машина проезжает километров за день: "))
m = int(input("Введите длину маршрута в километрах: "))
print((m + n - 1) // n)