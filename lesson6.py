# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
#(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep

class TrafficLight:

    color = ['red', 'yellow', 'green']
    delay = [7, 3, 2]

    def running(color, delay):
        '''Включаем свет на определенный интервал времени'''
        stage = 0
        for i in range(1, 5):
            print(f'{color[stage % 3]}')
            sleep(delay[stage % 3])
            stage += 1

color_now = TrafficLight
color_now.running(color_now.color, color_now.delay)


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._weight_1sm = 25
        self._depth = 10

    def get_weight(self):
        return self._depth * self._width * self._length * self._weight_1sm / 1000

total = Road(5000, 20)
print(f'{total.get_weight()} т')

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    """Базовый класс работника"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def get_income(self):
        raise NotImplementedError

class Position(Worker):
    """Класс сотрудника"""

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_user_name(self):
        """Метод возвращающий полное имя сотрудника"""
        return (f'{self.name} {self.surname}')

    def get_total_income(self):
        """Метод возвращающий полную зарплату сотрудника"""
        total = self._income['wage'] + self._income['bonus']
        return total

user = Position('Иван', 'Иванов', 'грузчик', 200, 60)
print(user.get_user_name())
print(user.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# Честно, совсем не понял задание


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self):
        self.title = 'неизвестной канцелярской принадлежностью'

    def draw(self):
        return f'Рисуем линию {self.title}'

class Pen(Stationery):

    def __init__(self):
        self.title = 'ручкой'

    def draw(self):
        return f'Рисуем линию {self.title}'


class Pencil(Stationery):

    def __init__(self):
        self.title = 'карандашом'

    def draw(self):
        return f'Рисуем линию {self.title}'


class Handle(Stationery):

    def __init__(self):
        self.title = 'марекром'

    def draw(self):
        return f'Рисуем линию {self.title}'


stat = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
print(f'{stat.draw()} \n{pen.draw()} \n{pencil.draw()} \n{handle.draw()}')