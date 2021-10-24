# структура данных Товары
list_products = []
i = 1
while True:
    name = input('Введите название: ')

    while True:
        price = input('Введите цену: ')
        if price.isdigit() == True:
            price = float(price)
            break
        else:
            print('Цена должна быть числом.')

    while True:
        qty = input('Введите количество: ')
        if qty.isdigit() == True:
            qty = int(qty)
            break
        else:
            print('Количество должно быть целым числом.')

    unit = input('Введите единицу измерения: ')

    tpl = (i, {'название': name,
          'цена': price,
          'количество': qty,
          'ед': unit
          })
    list_products.append(tpl)
    out = input('Если Вы добавили все товары, введите y: ')
    if out == 'y':
        break

    i += 1

print(f'Ваш список товаров:{list_products}')

dict_products = {}
i = 0
for i in range(len(list_products)):
    for key, value in list_products[i][1].items():
        if key in dict_products:
            if value not in dict_products.get(key):
                dict_products.get(key).append(value)
        else:
            dict_products.update({key: [value]})

    i += 1

print(f'Аналитика: {dict_products}')