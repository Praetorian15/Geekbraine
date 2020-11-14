# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['name', 12, True, None, ('name', 'age'), ['name'], {'city': 'Moscow'}, {1, 2}]
for el in my_list:
    print(type(el))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list2 = input('Введите список: ').split()

el = 0
for i in range(len(my_list2) // 2 ):
    my_list2[el], my_list2[el + 1] = my_list2[el + 1], my_list2[el]
    el += 2

print(my_list2)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = input('Введите номер месяца (число от 1 до 12): ')
while not month.isdigit() or int(month) <= 0 or int(month) > 12:
    month = input('Ошибка. Введите номер месяца (число от 1 до 12): ')

month = int(month)
if month == 12:
    month = 0
season = month // 3

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
print(seasons_list[season])

seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
print(seasons_dict[season])


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_text = input('Введите строку: ').split()
enumerate_list = enumerate(user_text)
for i, el in enumerate_list:
    print(i +1, el[:10])


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
new_el = input('Введите новый элемент рейтинга: ')
while not new_el.isdigit():
    new_el = input('Ошибка. Введите целое число: ')

new_el = int(new_el)
for el in my_list:
    if new_el > el:
        my_list.insert(my_list.index(el), new_el)
        break

    elif new_el < min(my_list):
        my_list.append(new_el)

print(my_list)




# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

name_list = []
price_list = []
quantity_list = []
measure_unit_list = []

# Ввод товара
query = 'y'
while query == 'y':
    name = input('Введите наименование товара: ')
    name_list.append(name)
    price = input('Введите стоимость товара: ')
    price_list.append(price)
    quantity = input('Введите количество товара товара: ')
    while not quantity.isdigit():
        quantity = input('Ошибка. Введите количество товара: ')
    quantity_list.append(quantity)
    measure_unit = input('Введите единицу измерения товара: ')
    measure_unit_list.append(measure_unit)
    query = input('Хотите ввести еще один товар? (y?): ')

# Формирование списка из кортежей с параметрами товара
goods = []
i = 0
for i in range(len(name_list)):
    product = {'Название': name_list[i], 'Цена': price_list[i], 'Количество': quantity_list[i], 'Ед': measure_unit_list[i] }
    i += 1
    product_tuple = (i, product)
    goods.append(product_tuple)
print(goods)

# Создание словаря

name_list = set(name_list)
price_list = set(price_list)
quantity_list = set(quantity_list)
measure_unit_list = set(measure_unit_list)

goods_dict = {'Название': list(name_list), 'Цена': list(price_list), 'Количество': list(quantity_list), 'Ед': list(measure_unit_list)}

print(goods_dict)

