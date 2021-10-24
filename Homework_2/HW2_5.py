# рейтинг, невозрастающая последовательность
num = int(input('Введите число: '))
my_list = [12, 7, 5, 3, 3, 2]

i = 0
for i in range(len(my_list)):
    if num > my_list[i]:
        my_list.insert(i, num)
        print(i) #для проверки, что одинаковые числа присоединились с правильными индексами
        break
    elif num <= my_list[-1]:
        my_list.append(num)
        break

print(my_list)
