"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
   реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
   создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
   Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print (f'{a} + {b} * i')

    def __add__(self, other):
        print(f'Сумма равна {self.a + other.a} + {self.b + other.b} * i')
        return ''

    def __mul__(self, other):
        print(f'Произведение {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i')
        return ''


x = Complex(5, 3)
y = Complex(4, -2)
print(x + y)
print(x * y)