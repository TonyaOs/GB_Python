'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
   выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('Task2.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(content)
    print(f'В файле {len(content)} строк')
    for i in range(len(content)):
        print(f'В {i+1} строке {len(content[i])} символов')



