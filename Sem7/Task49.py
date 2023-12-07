# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(orbit):
#     orb = map(list, orbits)
#     max_val = 0
#     max_t = ()

#     for a, b in orb:
#         s = 3.14 * a * b
#         if s / a == s / b:
#             continue
#         elif max_val < s:
#             max_val = s
#             max_t = (a, b)
#     return max_t


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

from math import pi


def find_farthest_orbit(orbits):
    print(max([orbit for orbit in orbits if orbit[0] != orbit[1]], key=lambda orb: pi * orb[0] * orb[1]))

    # макс применяет ко всем элементам функции Lambda значение key


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

find_farthest_orbit(orbits)

# def find_farthest_orbit(orbits):
#     del_circle_orbit = [axle_shaft for axle_shaft in orbits if axle_shaft[0] != axle_shaft[1]]
#     s_orbits = [axle_shaft[0] * axle_shaft[1] * 3.14 for axle_shaft in del_circle_orbit]
#     index = [i for i in range(len(s_orbits)) if s_orbits[i] == max(s_orbits)]
#     return del_circle_orbit[index[0]]


# orbit = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbit))

