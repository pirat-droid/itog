'''
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class OfficeEquipment:

    def __init__(self, name=None):
        self.name = name
        # self.list_office_equipment = {'name': name, 'price': price, 'count': count, 'office': office}
        self.list_office_equipment = {}

    def validate(self):
        name = input('Введите имя: ')
        price = input('Введите стоимость: ')
        try:
            price = int(price)
        except ValueError:
            return f'ошибка ввода данных'
        count = input('Введите количество: ')
        try:
            count = int(count)
        except ValueError:
            return f'ошибка ввода данных'
        office = input('Введите подразделение: ')
        self.list_office_equipment = {'name': name, 'price': price, 'count': count, 'office': office}
        return self.list_office_equipment

    def __str__(self):
        return f"наименование: {self.list_office_equipment['name']} цена: " \
               f"{self.list_office_equipment['price']} количество:" \
               f"{self.list_office_equipment['count']} офис: {self.list_office_equipment['office']}"


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
    print(OfficeEquipment().validate())
