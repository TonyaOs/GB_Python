'''
6. Реализовать два небольших скрипта:
   а) итератор, генерирующий целые числа, начиная с указанного,
   б) итератор, повторяющий элементы некоторого списка, определенного заранее.
   Подсказка: использовать функцию count() и cycle() модуля itertools.
   Обратите внимание, что создаваемый цикл не должен быть бесконечным.
   Необходимо предусмотреть условие его завершения.
   Например, в первом задании выводим целые числа, начиная с 3, а при достижении
   числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
   при котором повторение элементов списка будет прекращено.
'''
def func1():
    from itertools import count

    num = int(input('Введите первое число: '))
    stop = int(input('Введите последнее число: '))

    for el in count(num):
        if el <= stop:
            print(el)
    else: break

func1()

def func2():
    from itertools import cycle
    my_list = [12, 45, 48, 'data']
    i = 0
    for el in cycle(my_list):
        i += 1
        if i > 15:
            break
        print(el)

func2()





