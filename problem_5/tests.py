import unittest
import main

class mainTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_num(self):
        from main import check_num
        main.DIGS = (11,12,13,14,15,16,17,18,19,20)

        self.assertEqual(check_num(232792560), 232792560, "Проверка числа 232792560")
        self.assertEqual(check_num(2520),False,'Проверка числа 2520')

        main.DIGS = (1,2,3,4,5,6,7,8,9,10)
        self.assertEqual(check_num(232792560), 232792560, "Проверка числа 232792560")
        self.assertEqual(check_num(2520),2520,'Проверка числа 2520')
        self.assertEqual(check_num(20),False,'Проверка числа 20')
        self.assertEqual(check_num(400),False,'Проверка числа 400')



    def test_product(self):
        from main import product
        self.assertEqual(product((1,2,3,4)), 24, "Произведение 1,2,3,4")
        self.assertEqual(product((100,3,11,24)), 79200, "Произведение 100,3,11,24")
        self.assertEqual(product((1.2,2.5,-2,45)), -270, "Произведение 1.2,2.5,-2,45")
        self.assertEqual(product((1,0,3,4)), 0, "Произведение 1,0,3,4")





if __name__ == '__main__':
    unittest.main()