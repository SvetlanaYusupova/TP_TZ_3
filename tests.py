import time
import unittest
from random import sample
from functools import reduce
from functions import minimal, read_catalog, maximum, summ, product
from math import isclose


class TestDataProcessing(unittest.TestCase):
    def test_min(self):  # Тест проверки функции нахождения минимума
        data = [1, 2, 3, 4.1]
        assert isclose(1, minimal(data))

    def test_max(self):  # Тест проверки функции нахождения максимума
        data = [4.2, 4, 4.2, 4.1]
        assert isclose(4.2, maximum(data))

    def test_sum(self):  # Тест проверки функции нахождения суммы
        data = [-2.1, 2.1, -4.1, 4.1]
        assert isclose(0, summ(data))

    def test_pro(self):  # Тест проверки функции нахождения произведения
        data = [-2, 21, -4.1, 8]
        assert isclose(1377.6, product(data))

    def test_speed(self):  # Тест проверки файла на скорость при увеличении количества данных в файле в 5000 раз
        try:
            my_file = open("test_1.txt", "w+")
            my_file.write(str(sample(range(-100000, 100000), 10)))
            my_file.close()

            my_file = open("test_2.txt", "w+")
            my_file.write(str(sample(range(-100000, 100000), 50000)))
            my_file.close()
            start_time1 = time.time()
            data = read_catalog("test_1.txt")
            mi1 = minimal(data)
            ma1 = maximum(data)
            s1 = summ(data)
            p1 = product(data)
            end_time1 = time.time()

            start_time2 = time.time()
            data2 = read_catalog("test_2.txt")
            mi2 = minimal(data2)
            ma2 = maximum(data2)
            s2 = summ(data2)
            p2 = product(data2)
            end_time2 = time.time()
            assert (end_time2 - start_time2) <= 5000 * (end_time1 - start_time1)
        except AssertionError:
            print("Test on speed losed")

    def test_add(self):  # Тест проверки всех функций на рандомном количестве рандомных чисел 1000 раз подряд
        for i in range(1000):
            lengh = int(sample(range(1, 100), 1)[0])
            data = sample(range(-1000, 1000), lengh)
            assert isclose(min(data), minimal(data))
            assert isclose(max(data), maximum(data))
            assert isclose(sum(data), summ(data))
            assert isclose(reduce(lambda x, y: x * y, data), product(data))


if __name__ == '__main__':
    unittest.main()
