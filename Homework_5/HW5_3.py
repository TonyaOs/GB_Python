'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
   и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
   вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''
with open('Task3.txt', 'r', encoding='utf-8') as f:
    poor = []
    salary = []
    employees = f.read().split('\n')
    print(f'Список сотрудников: \n {employees} \n')

    for i in employees:
        i = i.split()
        if int(i[len(i)-1]) < 20000:
            poor.append(i[0] + ' ' + i[1])
            salary.append(int(i[len(i)-1]))
        else: salary.append(int(i[len(i)-1]))

    print(f'Малоимущие сотрудники: \n {poor} \n')
    print(f'Средний оклад {sum(salary)/len(salary)}')

