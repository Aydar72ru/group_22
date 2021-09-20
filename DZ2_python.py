# 1) Создать 2 переменных типа String с разными значениями
name = 'Aidar'
print(type(name))
name2 = 'Anton'
print(type(name2))

# 2) Создать 4 переменных типа Integer с разными значениями
counter_1 = 4
print(type(counter_1))
counter_2 = 12
print(type(counter_2))
counter_3 = 50
print(type(counter_3))
counter_4 = 80
print(type(counter_4))

# 3)Создать 3 переменных типа Float с разными значениями
miles_1 = 3.5
print(type(miles_1))
miles_2 = 4.5
print(type(miles_2))
miles_3 = 105.32
print(type(miles_3))

# 4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.

# Примеры со знаком больше '>' 3 примера (int)
A_1 = 5
A_2 = 6
print(A_1 > A_2)

A_1 = 8
A_2 = 6
print(A_1 > A_2)

A_1 = 7
A_2 = 7
print(A_1 > A_2)

# Примеры со знаком меньше '<' 3 примера (int)
A_1 = 9
A_2 = 10
print(A_1 < A_2)

A_1 = 12
A_2 = 10
print(A_1 < A_2)

A_1 = 12
A_2 = 12
print(A_1 < A_2)

# Примеры со знаком больше или равно '>=' 3 примера (int)
A_1 = 12
A_2 = 10
print(A_1 >= A_2)

A_1 = 12
A_2 = 12
print(A_1 >= A_2)

A_1 = 8
A_2 = 10
print(A_1 >= A_2)

# Примеры со знаком меньше или равно '<=' 3 примера (int)
A_1 = 9
A_2 = 10
print(A_1 <= A_2)

A_1 = 12
A_2 = 10
print(A_1 <= A_2)

A_1 = 10
A_2 = 10
print(A_1 <= A_2)

# Примеры со знаком не равно '!=' 3 примера (int)
A_1 = 10
A_2 = 10
print(A_1 != A_2)

A_1 = 9
A_2 = 10
print(A_1 != A_2)

A_1 = 12
A_2 = 10
print(A_1 != A_2)

# 5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.

# Примеры со знаком больше '>' 2 примера (float)
B_1 = 5.8
B_2 = 6.7
print(B_1 > B_2)

B_1 = 8.1
B_2 = 6.6
print(B_1 > B_2)

# Примеры со знаком больше '<' 2 примера (float)
B_1 = 9.9
B_2 = 10.3
print(A_1 < A_2)

A_1 = 12.8
A_2 = 10.1
print(A_1 < A_2)

# Примеры со знаком больше или равно '>=' 2 примера (float)
A_1 = 12.2
A_2 = 10.7
print(A_1 >= A_2)

A_1 = 12.5
A_2 = 12.4
print(A_1 >= A_2)

# Примеры со знаком меньше или равно '<=' 2 примера (float)
A_1 = 9.3
A_2 = 10.3
print(A_1 <= A_2)

A_1 = 12.9
A_2 = 10.4
print(A_1 <= A_2)

# Примеры со знаком не равно '!=' 3 примера (float)
A_1 = 11.5
A_2 = 10.7
print(A_1 != A_2)

A_1 = 9.3
A_2 = 10.7
print(A_1 != A_2)

# 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.

# Пример со знаком больше ('>' and) два примера.
A = 4 > 2
B = 5 > 3
print(A and B)

A = 4 > 8
B = 5 > 9
print(A and B)

# Пример со знаком больше ('<' and) во втором добавил ('<' '>' and) два примера.

A = 50 < 80
B = 99 < 208
print(A and B)

A = 1 < 9
B = 9 > 8
print(A and B)

# Пример со знаком больше ('>=' and) два примера
A = 9 >= 9
B = 10 >= 10
print(A and B)

A = 9 >= 90
B = 10 >= 105
print(A and B)

# Пример со знаком больше ('!=' or) два примера
age = 30
height = 186
print(age != 30 or height != 186)

A = 30 != 37
B = 45 != 46
print(A or B)

# Пример со знаком больше ('<' not) два примера

A = 50 < 100
print(A)

A = 50 < 10
print(A)

# 7) Сделать скрипт используя функцию input().
   # 1. Функция должна на вход принимать целое число.
   # 2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"

print('Введите число')
x = int(input())
if x < 30:
    print(f"{x}<30")
elif x > 30:
    print(f"{x}>30")
else:
    print(f"{x}==30")

# 8) Сделать скрипт используя функцию input().
    #1. Функция должна на вход принимать целое число.
    #2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
    #3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"

print('Введите число:')
import random
x = int(random.randint(1, 100))
print(x)
y = int(input())
if x < y:
    print(print(f"{x}<{y}"))
elif x > y:
    print(print(f"{x}>{y}"))
else:
    print(print(f"{x}=={y}"))

# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
import random
print('Введите')
a = int(input())
x = random.randint(1, 100)
print(f"{x}")
y = random.randint(1, 100)
print(f"{y}")
if (a < x) and (a < y):
    print(print(f"{a}<{x}")) and print(print(f"{a}<{y}"))
elif (a > x) and (a > y):
    print(print(f"{a}>{x}")) and print(print(f"{a}>{y}"))
elif (a < x) and (a > y):
    print(print(f"{a}<{x}")) and print(print(f"{a}>{y}"))
elif (a > x) and (a < y):
    print(print(f"{a}>{x}")) and print(print(f"{a}<{y}"))
elif (a == x) and (a > y):
    print(print(f"{a}=={x}")) and print(print(f"{a}>{y}"))
elif (a == x) and (a < y):
    print(print(f"{a}=={x}")) and print(print(f"{a}<{y}"))
elif (a > x) and (a == y):
    print(print(f"{a}>{x}")) and print(print(f"{a}=={y}"))
elif (a < x) and (a == y):
    print(print(f"{a}<{x}")) and print(print(f"{a}=={y}"))
else:
    print(print(f"{a}=={x}")) and print(print(f"{a}=={y}"
