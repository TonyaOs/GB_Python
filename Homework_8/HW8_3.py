"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
   только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя
   данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
"""

class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    num = input("Введите число (чтобы выйти введите 'out'): ")
    try:
        if num.isdigit() == False:
            raise ZeroException("Вы ввели не число")
    except ZeroException as err:
        print(err)
    else:
        my_list.append(int(num))
    if num == "out":
        break

print(my_list)
