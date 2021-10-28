def summation(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers = input('Введите числа через пробел: ')
    sum, flag = summation(*numbers.split(' '))
    general_sum += sum
    print(f'Общая сумма {general_sum}')

    if flag:
        break



