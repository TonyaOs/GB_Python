"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
   Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
   в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt

num = int(input("Введите число: "))
divider = int(input("Введите делитель: "))
try:
    if divider == 0:
        raise ZeroException("На ноль делить нельзя")
except ZeroException as err:
    print(err)
else:
    print(num / divider)
