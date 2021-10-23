x = int(input('Введите время в секундах: '))
second = x%60
minute = x//60
hours = minute//60
minute_ost = minute%60

print(f"{hours:02}:{minute_ost:02}:{second:02}")