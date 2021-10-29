# разбить строку на слова и пронумеровать их
words = input('Введите строку: ').split()

for ind, el in enumerate(words):
    print(ind, el[:10])