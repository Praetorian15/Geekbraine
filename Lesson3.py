# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Делитель не может быть 0'

def check_number(number):
    while True:
        try:
            number = float(number)
            break
        except ValueError:
            number = input('Неверный формат. Попробуйте еще раз: ')

div_1 = input('Введите делимое: ')
check_number(div_1)

div_2 = input('Введите делитель: ')
check_number(div_2)

print(my_div(float(div_1), float(div_2)))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def user_info(name = 'Эльдар',last_name = 'Меркулов', birth_year = '1984', city = 'Москва', email = 'em@yandex.ru', phone = '1111111'):
    return (f'{last_name} {name} {birth_year} {city} {phone} {email}')

print(user_info())


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    list_numb = [num_1, num_2, num_3]
    list_numb.remove(min(list_numb))
    return sum(list_numb)

print(my_func(15, 8, 6))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def deg_num_1(x, y):                # Через **
    return 1 / x ** abs(y)

def deg_num_2(x, y):                # Через цикл
    result = 1
    for i in range(0, abs(y)):
        result *= 1 / x
    return result

num_1 = input('Введите действительное положительное число x: ')    #Проверку сделать не успеваю
num_2 = input('Введите степень, целое отрицательное число y: ')

print(deg_num_1(num_1, num_2))
print(deg_num_2(num_1, num_2))


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

def user_sum(data):  # Вычисление суммы после ввода каждой строки
    data = data.replace(',', '.')
    user_num_list = data.split()
    for i, item in enumerate(user_num_list):
        if item.upper() == 'N':
            user_num_list.remove(item)
            break
        else:
            try:
                old_item = item
                user_num_list[i] = float(old_item)
            except ValueError:
                return 0

    return sum(user_num_list)

result = 0
while True:                     # Ввод данных от пользователя и суммирование промежуточных результатов
    user_num = input('Введите числа через пробел (для завершения работы введите "n"): ')
    if user_num[-1] == 'n':
        result += user_sum(user_num)
        break
    else:
        result += user_sum(user_num)
        print(result)


print(result)


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# def int_func(word):
#     return word.capitalize()
#
# sent = 'hi my name is eldar'
# sent_list = sent.split()
# result = []
# for i in sent_list:
#     i = int_func(i)
#     result.append(i)
#
# print(' '.join(result))