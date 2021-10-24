# времена года list
month = int(input('Введите номер месяца: '))
month_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

i=0
for i in range(len(month_list)):
    if (month_list[i].count(month)) > 0:
        if i == 0: print('winter')
        elif i == 1: print('spring')
        elif i == 2: print('summer')
        elif i == 3: print('autumn')

if month > 12 or month < 1 :
    print('Вы ввели неверное число')

print()
# времена года dict
month = int(input('Введите номер месяца: '))

month_dict = {1: 'winter',
              2: 'winter',
              12: 'winter',
              3: 'spring',
              4: 'spring',
              5: 'spring',
              6: 'summer',
              7: 'summer',
              8: 'summer',
              9: 'autumn',
              10: 'autumn',
              11: 'autumn'}

if month > 12 or month < 1 :
    print('Вы ввели неверное число')
else:
    print (month_dict[month])

