'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def extraction(cls, data):
        arr_data = []
        for i in data.split('-'):
            arr_data.append(int(i))
        return arr_data

    @staticmethod
    def valid(data):
        if (data[0]) < 1 or (data[0] > 31):
            print(f'День введен не корректно')
        elif data[1] < 1 or data[1] > 12:
            print(f'Месяц введен не корректно')
        elif data[1] < 2020 or data[1] > 2023:
            print(f'Год введен не корректно')
        else:
            print(f'Текущая дата {data}')


if __name__ == '__main__':
    data = Data.extraction('45-10-2022')
    Data.valid(data)
