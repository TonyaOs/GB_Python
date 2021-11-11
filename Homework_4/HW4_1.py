from sys import argv

name_script, qty, cost, bonus = argv

print(name_script)

def calculate(qty, cost, bonus):
    result = ((float(qty) * float(cost)) + float(bonus))
    return result

print (f'Всего начисленно: {calculate(qty, cost, bonus)}')
