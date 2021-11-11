"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
   В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
   В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
   вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
   только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
   соответственно. В методе деления должно осуществляться округление значения до целого числа.
   В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
   Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
   где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
   то в последний ряд записываются все оставшиеся.
   Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
   вернет строку: *****\n*****\n**.    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
   Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""
class Cell:
    def __init__(self, qty):
        self.qty = int(qty)
        print("*" * self.qty)

    def __add__(self, other):
        return self.qty + other.qty

    def __sub__(self, other):
        if self.qty <= other.qty:
            return str(f"Если вы это сделаете, клетки аннигилируют")
        else:
            return self.qty - other.qty

    def __mul__(self, other):
        return self.qty * other.qty

    def __truediv__(self, other):
        return round(self.qty / other.qty)

    def make_order(self, qty_in_row):
        row = self.qty // qty_in_row
        ost = self.qty % qty_in_row
        for i in range(row):
            print("*" * qty_in_row)
        print("*" * ost)

cell1 = Cell(10)
cell2 = Cell(14)
cell1.make_order(3)
print(cell1 - cell2)
print(cell1 + cell2)
print(cell2 / cell1)
print(cell1 * cell2)
