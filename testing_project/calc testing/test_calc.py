import unittest
import calc

class testCalc(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setUpClass \n')


    @classmethod
    def tearDownClass(self):
        print('tearDownClass')
        

    def setUp(self):
        print("setUp")
    

    def tearDown(self):
        print("tearDown \n")


    def test_add(self):
        print('test_add')
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


    def test_subtract(self):
        print('test_subtract')
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)


    def test_mutiply(self):
        print('test_mutiply')
        self.assertEqual(calc.mutiply(10, 5), 50)
        self.assertEqual(calc.mutiply(-1, 1), -1)
        self.assertEqual(calc.mutiply(-1, -1), 1)


    def test_divide(self):
        print('test_divide')
        self.assertEqual(calc.divide(10, 5), 2)    
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        self.assertRaises(ZeroDivisionError, calc.divide, 10, 0)

        # with self.assertRaises(ZeroDivisionError): # context manager
        #     calc.divide(10, 2)
            

if __name__ == "__main__":
    unittest.main()