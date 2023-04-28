'''
5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
'''


class OfficeEquipment:

    def __init__(self, name: [str], price: [int], count: [int], office: [str]):
        self.name = name
        self.list_office_equipment = {'name': name, 'price': price, 'count': count, 'office': office}

    def __str__(self):
        return f"наименование: {self.list_office_equipment['name']} цена: "\
                f"{self.list_office_equipment['price']} количество:"\
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
    print(OfficeEquipment('hp', 2, 2, 'Головной'))
