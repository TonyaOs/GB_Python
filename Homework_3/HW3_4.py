def my_func(x, y):
    return x ** y

def my_func1(x, y):
    result = 1
    for i in range(abs(y)):
        result = x*result
        i += 1
    return 1/result

print(my_func(x = float(input('Введите действительное число: ')),
              y = int(input('Введите отрицательное целое число: '))
              ))

print(my_func1(x = float(input('Введите действительное число: ')),
              y = int(input('Введите отрицательное целое число: '))
              ))



