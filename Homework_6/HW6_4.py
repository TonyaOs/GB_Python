"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
   color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
   что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
   SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
   текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
   Выполните вызов методов и также покажите результат.
"""
class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f" {self.name} поехала")

    def stop(self):
        print(f" {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f" {self.name} повернула {self.direction}")

    def show_speed(self):
        print(f" {self.name} двигается со скоростью {self.speed} км/ч")


class TownCar(Car):
    def Town(self):
        if self.speed > 60:
            print(f" {self.name} ваша скорость больше 60 км/ч, снизьте скорость")
        else:
            print(f"Скорость в пределах нормы")


class SportCar(Car):
    def sport(self):
        print(f" {self.name} спортивная машина")


class WorkCar(Car):
    def work(self):
        if self.speed > 40:
            print(f" {self.name} ваша скорость больше 40 км/ч, снизьте скорость")
        else: print(f"Скорость в пределах нормы")


class PoliceCar(Car):
    def police(self):
        print(f" Это полицейская машина")

car1 = SportCar(120, "grey", "Аudi")
car1.sport()
car1.go()
car1.show_speed()
car1.turn("налево")
car1.stop()
print()
car2 = WorkCar(60, "yellow", "MAN")
car2.go()
car2.show_speed()
car2.work()
car2.turn("налево")
car2.stop()
print()
car3 = PoliceCar(100, "blue", "Reno", True)
car3.police()
car3.go()
car3.show_speed()
car3.turn("направо")
car3.stop()