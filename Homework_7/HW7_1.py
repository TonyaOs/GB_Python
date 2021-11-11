"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
   конструктора класса (метод __init__()), который должен принимать данные
   (список списков) для формирования матрицы.
   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
   класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""

class Matrix:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(el)

    def __str__(self):
        for i in self.my_list:
            for j in i:
                print (f"{j}", end = "  ")
            print()
        return '' # почему здесь надо делать return?

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return self.my_list

obj = Matrix([1,2,3], [7,8,9])
obj2 = Matrix([4,5,6], [3,2,1])
print(obj)
print(obj2)
obj.__add__(obj2)
print(obj)

