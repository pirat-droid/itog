'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class MyClass:

    def __init__(self, number: [int], delitel: [int]):
        self.number = number
        self.delitel = delitel

    def get_result(self):
        if self.delitel == 0:
            return f'Делитель не должен быть равен нулю'
        else:
            return str(self.number / self.delitel)


if __name__ == '__main__':
    print(MyClass(10, 2).get_result())
