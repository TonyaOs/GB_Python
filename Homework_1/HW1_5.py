# выручка и издержки фирмы
revenue = int(input('Введите выручку: '))
outlay = int(input('Введите издержки: '))

if outlay > revenue:
    print('Фирма работает в убыток {} рублей'.format(outlay - revenue))
else:
    profit = revenue - outlay
    print ('Фирма получает прибыль {} рублей'.format(profit))
    print('Рентабельность выручки: {}'.format(profit/revenue))
    emploees = int(input('Введите численность сотрудников: '))
    print ('В расчете на одного сотрудника: {} рублей'.format(profit/emploees))