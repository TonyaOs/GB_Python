'''
4. Создать (не программно) текстовый файл со следующим содержимым:
   One — 1
   Two — 2
   Three — 3
   Four — 4
   Необходимо написать программу, открывающую файл на чтение и считывающую
   построчно данные. При этом английские числительные должны заменяться на русские.
   Новый блок строк должен записываться в новый текстовый файл.
'''
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре', 'Five' : 'Пять'}
Task4_new = []
with open('Task4.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split()
        Task4_new.append(rus[i[0]] + ' ' + i[1] + ' ' + i[2] + '\n')
    print(Task4_new)

with open('Task4_new.txt', 'w', encoding='utf-8') as f:
    f.writelines(Task4_new)

