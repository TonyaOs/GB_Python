"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
   А также класс «Оргтехника», который будет базовым для классов-наследников.
   Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
   В базовом классе определить параметры, общие для приведенных типов.
   В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
   на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
   и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
   например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
   Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

class Stock:
    my_dict = {}
    while (True):
        try:
            name_unit = input("Введите тип оборудования (выход - пустой enter)")
            if name_unit == '':
                break
            qty_unit = int(input("Введите количество"))
        except:
            print("Ошибка ввода данных")
        my_dict[name_unit] = qty_unit

    def __init__(self, type_stock):
        self.type_stock = type_stock

        print(f"На складе {self.type_stock} в наличии: {Stock.my_dict}")

    def give_away(self, name_unit, qty ):
        remains = Stock.my_dict[name_unit] - qty
        return print(f"На складе осталось {remains} {name_unit}")


class Equipment:
    def __init__(self, type_equipment, model, price, department, qty):
        self.type_equipment = type_equipment
        self.model = model
        self.price = price
        self.department = department
        self.qty = qty

    def to_department(self):
        print(f"В департамент {self.department} передано {self.qty} {self.type_equipment}")

class Printer(Equipment):
    def __init__(self, type_equipment, model, price, department, qty, color):
        super().__init__(type_equipment, model, price, department, qty)
        self.color = color
        print (f"{type_equipment} {self.model} {self.color} {self.qty} шт")


class Scaner(Equipment):
    def __init__(self, type_equipment, model, price, department, qty, mass):
        super().__init__(type_equipment, model, price, department, qty)
        self.mass = mass
        print (f"{type_equipment} {self.model} весит {self.mass} кг")

class Xerox(Equipment):
    def __init__(self, type_equipment, model, price, department, qty, type):
        super().__init__(type_equipment, model, price, department, qty)
        self.type = type
        print (f"{type_equipment} {self.model} типа {self.type}")

stock_equipment = Stock("Оборудование")
printer1 = Printer("Принтер", "HP-258", 4500, "Analytics", 2, "color")
printer1.to_department()
stock_equipment.give_away("Принтер",2)

scaner1 = Scaner("Сканер", "Scan-520", 7000, "Accounting", 3, 35)
scaner1.to_department()
stock_equipment.give_away("Сканер",3)

xerox1 = Xerox("Ксерокс", "X-541", 9000, "Management", 1, "office")
