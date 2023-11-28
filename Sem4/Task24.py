# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки

arr = [5, 8, 6, 4, 9, 2, 7, 3]
max1 = 0
for i in range (len(arr)):
    if arr[i] + arr[i - 1] + arr[i -2] > max1:
        max1 = arr[i] + arr[i - 1] + arr[i - 2]
    else:
        continue
    i += 1
print(max1)

arr = [5, 8, 6, 4, 9, 2, 7, 3]

module_size = 3
fragmet_sets = {0,}

array_size = len(arr) - 1

index = array_size
while index != -1:
    fragmet_sum = 0
    for item in range(module_size):
        fragmet_sum = arr[index] + arr[index - 1] + arr[index - 2]
    fragmet_sets.add(fragmet_sum)
    index -= 1

print(
    max(fragmet_sets)
)
    