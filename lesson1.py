# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

number = 1
print(f'{number} - это {type(number)}')
number2 = 1.4
print(f'{number2} - это {type(number2)}')
bool_ex = True
print(f'{bool_ex} - это {type(bool_ex)}')
user = input('Введите любые символы: ')
print(f'{user} - это {type(user)}')
user1 = int(input('Введите любое целое число: '))
print(f'{user1} - это {type(user1)}')
cities = ["Москва", "Санкт-Петербург", "Казань"]
print(f'{cities} - это {type(cities)}')
role = ('admin', 'user', 'guest')
print(f'{role} - это {type(role)}')
result = {'Ivanov: 2', 'Petrov: 3', 'Sidorov: 1'}
print(f'{result} - это {type(result)}')

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Введите время в секундах: '))
hour = user_time // 3600
minute = user_time % 3600 // 60
second = user_time % 60
print(f'Время пользователя: {hour}:{minute}:{second}')
Либо
print(f'Время пользователя: {user_time // 3600}:{user_time % 3600 // 60}:{user_time % 60}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input('Введите любое число: ')
user_number_double = user_number + user_number
user_number_triple = user_number + user_number + user_number
result = int(user_number) + int(user_number_double) + int(user_number_triple)

print(f'{user_number} + {user_number_double} + {user_number_triple} = {result}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_number = input('Введите целое положительное число больше 10: ')

count = len(user_number)
max_number = '0'

while count > 0:
    count -=1
    if user_number[count] > max_number:
        max_number = user_number[count]

print(f'Наибольшая цифра в числе {max_number}')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = float(input('Введите доходы вашей фирмы: '))
loss = float(input('Введите расходы вашей фирмы: '))
profit = income - loss
if profit < 0:
    print('Ваша фирма убыточна.')
else:
    profit_2 = profit / income
    number_of_employees = int(input('Введите численность сотрудников вашей фирмы: '))
    profit_empl = profit / number_of_employees
    print(f'Рентабельность выручки: {round(profit_2, 2)}')
    print(f'Прибыль фирмы в расчете на одного сотрудника: {round(profit_empl, 2)}')



# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

start = int(input('Введите результат первого дня в километрах: '))
target = int(input('Введите желаемый результат в километрах: '))

count = 1
current_result = start
print('Результат:')
print(f'{count} - й день: {current_result}')

while current_result < target:
    count += 1
    current_result = current_result * 1.1
    print(f'{count} - й день: {current_result}')

print(f'На {count}-й день спортсмен достиг результата — не менее {target} км.')
