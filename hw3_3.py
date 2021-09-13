# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    return sum(sorted(my_list)[1:])


print(my_func(42, 11, 5))

my_func = lambda num_1, num_2, num_3: (num_1 + num_2 + num_3) - min(num_1, num_2, num_3)
