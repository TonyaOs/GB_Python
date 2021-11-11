"""
5. Реализовать класс Stationery (канцелярская принадлежность).
   Определить в нем атрибут title (название) и метод draw (отрисовка).
   Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
   Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
   реализовать переопределение метода draw. Для каждого из классов методы
   должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
   что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручкой ({self.title})")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандашом ({self.title})")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркером ({self.title})")


num1 = Stationery("Ручка")
num1.draw()
print()
num2 = Pencil("Карандаш")
num2.draw()
print()
num3 = Handle("Маркер")
num3.draw()
print()
num4 = Pen("Ручка")
num4.draw()