# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def f (a, b):
    if b == 0:
        return a
    else:
        return 1 + f(a, b-1)

a = 4
b = 2
print(f(a, b))