import main
import unittest


class MainTest(unittest.TestCase):

    def test_del_count(self):
        from main import del_count
        self.assertEqual(del_count(1),1,'test num 3')
        self.assertEqual(del_count(3),2,'test num 3')
        self.assertEqual(del_count(6),4,'test num 6')
        self.assertEqual(del_count(10),4,'test num 10')
        self.assertEqual(del_count(28),6,'test num 28')
        self.assertEqual(del_count(31),2,'test num 2')
        self.assertEqual(del_count(4),3,'test num 4')
        self.assertEqual(del_count(16),5,'test num 16')
        #self.assertEqual(del_count(2982840),128,'test num 2982840') # 0.4+ seconds
        #self.assertEqual(del_count(76576500),576,'test num 76576500') # 12+ seconds



    def test_del_count2(self):
        from main import del_count2
        self.assertEqual(del_count2(1),1,'test num 3')
        self.assertEqual(del_count2(3),2,'test num 3')
        self.assertEqual(del_count2(6),4,'test num 6')
        self.assertEqual(del_count2(10),4,'test num 10')
        self.assertEqual(del_count2(28),6,'test num 28')
        self.assertEqual(del_count2(31),2,'test num 2')
        self.assertEqual(del_count2(4),3,'test num 4')
        self.assertEqual(del_count2(16),5,'test num 16')
        #self.assertEqual(del_count2(2982840),128,'test num 2982840')
        self.assertEqual(del_count2(76576500),576,'test num 76576500') #fast 0.01 sec


if __name__ == "__main__":
    unittest.main(verbosity=True)


    pass


