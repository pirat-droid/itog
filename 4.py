'''
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
'''


class OfficeEquipment:

    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):

    def get_printer(self):
        return f'принтер {self.name}'

class Scaner(OfficeEquipment):

    def get_scaner(self):
        return f'сканер {self.name}'


class Xerox(OfficeEquipment):

    def get_xerox(self):
        return f'ксерокс {self.name}'


if __name__ == '__main__':
    print(Printer('hp').get_printer())
    print(Scaner('cannon').get_scaner())
    print(Xerox('xerox').get_xerox())
