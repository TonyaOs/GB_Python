def division(x, y):
    if x.isdigit() == True and y.isdigit() == True:
        if float(y) == 0:
            print('Делить на ноль нельзя, повторите ввод')
        else: return float(x)/float(y)
    else: print('Вводимые данные не являются числом')

while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    print(division(a,b))
    stop = input('Есди вы закончили расчеты нажмите y: ')
    if stop == 'y':
        break