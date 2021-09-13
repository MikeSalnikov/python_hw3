# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


# # x = 2
# # y = -4
# # result = 1
#
# for i in range(abs(y)):
#     result *=x
#
# if n < 0:
#     re = 1 / result
#
# print((f'{x}**{n}==', result))
#
# def pow_func(x, y):
#     if y == 0:
#         return 1
#     else:
#         factor = pow_func(x, y//2)
#         if y%2 == 0:
#             return factor * factor
#         else:
#             return factor * factor * x

def my_pow_func(x, y):
    return 1 if y == 0 else my_pow_func(x, y + 1) * 1 / x

print(my_pow_func(3, -2))