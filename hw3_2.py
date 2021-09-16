# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def get_person(**kwargs):
    return ' '.join(kwargs.values())


name = input('Введите name - ')
surname = input('Введите surname - ')
birthday = input('Введите birthday - ')
city = input('Введите city - ')
email = input('Введите email - ')
phone = input('Введите phone - ')

print(get_person(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))