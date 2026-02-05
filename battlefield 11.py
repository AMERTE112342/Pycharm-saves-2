# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)
# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         break
# if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
# n = int(input())
# flag = False
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 7:
#         flag = True
#         break
#     n //= 10
# if flag == True:
#     print('Число', n, 'содержит цифру 7')
# else:
#     print('Число', n, 'не содержит цифру 7')
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue
#     print(i)
# for i in range(10):
#     print(i, end = '*')
#     if i > 6:
#         break
# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)
# mult = 1
# for i in range(1, 11):
#     if i % 2 == 0:
#       continue
#     if i % 9 == 0:
#         break
#     mult *= i
# print(mult)
# a = 1
# for i in range(1,1000):
#     if i % 2 == 1:
#         a = a + 1
# print(a)
# n = int(input())
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(fatorial)
# a = int(input())
# b = 0
# c = 0
# while a != -1:
#     if a > 7:
#         b = b + a
#         c = c + 1
#     a = int(input())
# print(b/c)
# for hours in range(24):
#     for minutes  in range(60):
#        for seconds in range(60):
#         print(hours, ':', minutes,':', seconds)
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i,j)
# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)
# for i in range(1, 4):
#     for j in range(3, 5):
#      print(i + j, end='')
# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)
# n = int(input())
# a =  n
# if n >= 10:
#    print('Больше')
# for i in range(n):
#     if n <= 0:
#      print('Меньше')
#         break
#     for b in range(3):
#            print(n,end='')
#      print(sep='')
n = int(input())
a =  n
if n >= 10:
   print('Больше')
for i in range(1, n + 1):
    if n <= 0:
     print('Меньше')
     break
    for b in range(1, 10):
        c = i * b
        print(i, '*', b, '=', c, end=' ')
        print(sep='\n')
    print(end='\n')


