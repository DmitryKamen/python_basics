# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

a = int(input("Введите долю a: "))
b = int(input("Введите долю b: "))
c = int(input("Введите долю c: "))
# m = a - 1
# res_b = 0
# n = b - 1
# res_a = 0
# flag = True 
# while n > 0 and m > 0 and flag:
#     res_b = b * m
#     res_a = a * n
#     if res_a == c or res_b == c:
#         print("yes")
#         flag = False
#     n -= 1
#     m -= 1
# if res_a != c and res_b != c: 
#     print("no")

# if (a < b and c >= a and c % a == 0 or b < a and c >= b and c % b == 0) and c < b * a:
#     print("yes")
# else:
#     print ('no')

if ( c % a == 0 or c % b == 0 ) and c < b * a:
    print("yes")
else:
    print ('no')




    

