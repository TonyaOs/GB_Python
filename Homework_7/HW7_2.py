"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
   Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
   К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
   размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
   Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
   для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
   Реализовать общий подсчет расхода ткани.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.parametr/6.5 + 0.5)


class Suit(Clothes):
    @property
    def consumption(self):
        return round(2 * self.parametr + 0.3)

suit1 = Suit(5)
print(f"На костюм: {suit1.consumption} метров")
coat1 = Coat(10)
print(f"На пальто: {coat1.consumption} метров")
print(f"Всего понадобится {coat1.consumption + suit1.consumption} метров ткани")




