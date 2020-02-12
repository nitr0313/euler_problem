import unittest
import main

class mainTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_variant(self): #variant(len_x,len_y,point_x,point_y)
        from main import variant
        self.assertEqual(variant(10,10,6,7,4),1,"Test 1 variant(10,10,6,7,4)")
        self.assertEqual(variant(10,10,6,6,4),4,"Test 4 variant(10,10,6,6,4)")
        self.assertEqual(variant(10,10,7,7,4),0,"Test 0 variant(10,10,7,7,4)")
        self.assertEqual(variant(10,10,7,6,4),2,"Test 2 variant(10,10,7,6,4)")

        self.assertEqual(variant(5,5,3,3,2),4,"Test 4 variant(5,5,5,3,2)")
        self.assertEqual(variant(5,5,5,0,2),2,"Test 2 variant(5,5,5,0,2)")

        self.assertEqual(variant(10,10,2,0,4),3,"Test 3 variant(10,10,2,0,4)")
        self.assertEqual(variant(10,10,3,0,4),4,"Test 4 variant(10,10,3,0,4)")
        self.assertEqual(variant(10,10,7,0,4),2,"Test 2 variant(10,10,7,0,4)")
        self.assertEqual(variant(10,10,6,0,4),4,"Test 4 variant(10,10,6,0,4)")

        # main.DIGS = (11,12,13,14,15,16,17,18,19,20)

        # self.assertEqual(check_num(232792560), 232792560, "Проверка числа 232792560")
        # self.assertEqual(check_num(2520),False,'Проверка числа 2520')

        # main.DIGS = (1,2,3,4,5,6,7,8,9,10)
        # self.assertEqual(check_num(232792560), 232792560, "Проверка числа 232792560")
        # self.assertEqual(check_num(2520),2520,'Проверка числа 2520')
        # self.assertEqual(check_num(20),False,'Проверка числа 20')
        # self.assertEqual(check_num(400),False,'Проверка числа 400')



    def test_product(self):
        from main import product
        self.assertEqual(product((1,2,3,4)), 24, "Произведение 1,2,3,4")
        self.assertEqual(product((100,3,11,24)), 79200, "Произведение 100,3,11,24")
        self.assertEqual(product((1.2,2.5,-2,45)), -270, "Произведение 1.2,2.5,-2,45")
        self.assertEqual(product((1,0,3,4)), 0, "Произведение 1,0,3,4")





if __name__ == '__main__':
    unittest.main()