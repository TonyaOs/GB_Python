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

#еще один способ
while True:
    user_month = input('Введите номер от 1 до 12: ')
    if user_month.isdigit() and 1 <= int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима' ]
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список - {season_1[int(user_month)//3]}\nСловарь - {season_2[int(user_month)//3]}')
        break
    else: print('Error')


