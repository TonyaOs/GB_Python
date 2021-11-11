'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
   При вызове функции должен создаваться объект-генератор.
   Функция должна вызываться следующим образом: for el in fact(n).
   Функция отвечает за получение факториала числа, а в цикле необходимо
   выводить только первые n чисел, начиная с 1! и до n!.
'''

from itertools import count
from math import factorial

def fact():
    for i in count(1):
        yield factorial(i)

num = int(input('Введите число: '))
x = 0
for el in fact():
    if x < num:
        print(el)
        x += 1
    else: break






