# обмен элементами
your_list = input('Введите элементы списка через запятую ')
your_list = list(your_list.split(','))

i = 0
for i in range(i, len(your_list)-1, 2):
    your_list[i], your_list[i+1] = your_list[i+1], your_list[i]

print(your_list)