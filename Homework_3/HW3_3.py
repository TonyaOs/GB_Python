def my_func(x, y, z):
    min_arg = min([x, y, z])
    return x + y + z - min_arg

print ('result = ',
               my_func(float(input('Введите x: ')),
               float(input('Введите y: ')),
               float(input('Введите z: '))
               )
       )



