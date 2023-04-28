'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class Complex:
    def __init__(self, a, b):
        self.__complex = complex(a, b)

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex + other
        return Complex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex * other
        return Complex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = Complex(1, -5)
    c2 = Complex(1, 2)
    print(c1 + c2, complex(6, -4) + complex(2))
    print(c1 * c2, complex(5, -3) * complex(3))
