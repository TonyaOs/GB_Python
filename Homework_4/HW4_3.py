'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
   Необходимо решить задание в одну строку.
'''

list1 = list(range(20, 240))
print(list1)

new_list = [el for el in list1 if el % 20 == 0 or el % 21 == 0]
print(new_list)