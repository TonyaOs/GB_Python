"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
   строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
   с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их
   тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
   месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
from datetime import date

class DateC:
    def __init__(self, my_date):
        self.my_date = my_date

    @classmethod        #для чего здесь может пригодиться cls?
    def type_int(cls, my_date):
        day, month, year = my_date.split(".")
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            return "Вы ввели буквы, а нужно цифры"
        return day, month, year

    @staticmethod
    def valid(my_date):
        day, month, year = my_date.split(".")
        try:
            print(date(int(year), int(month), int(day)))
        except ValueError:
            return "Такой даты не существует"
        return ''

print(DateC.valid("73.12.2021"))
print(DateC.valid("23.12.2021"))
print(DateC.type_int("15.12.2021"))
print(DateC.type_int("AARRR.12.2021"))