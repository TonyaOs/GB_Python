'''
7. Создать (не программно) текстовый файл, в котором каждая строка
   должна содержать данные о фирме: название, форма собственности, выручка, издержки.
   Пример строки файла: firm_1 ООО 10000 5000.
   Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
   а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
   Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
   а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
   Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
   Итоговый список сохранить в виде json-объекта в соответствующий файл.
   Пример json-объекта:
   [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

   Подсказка: использовать менеджеры контекста.
'''
import json
profit = {}
pr = {}
prof = 0
prof_average = 0
i = 0
with open('Task7.txt', 'r') as f:
    for line in f:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = prof / i
        print(f'Средняя прибыль - {prof_average:.2f}')
    else:
        print(f'Средняя прибыль отсутсвует')
    pr = {'Средняя прибыль': round(prof_average)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('Task7_j.json', 'w') as fs:
    json.dump(profit, fs)

    js_str = json.dumps(profit)
    print(f'Создан файл json, его содержимое: \n '
          f' {js_str}')