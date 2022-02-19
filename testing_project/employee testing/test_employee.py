from employee import Employee
import unittest
from unittest.mock import patch


class testEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setUpClass \n')


    @classmethod
    def tearDownClass(self):
        print('tearDownClass')
        
        
    def setUp(self):
        print("setUp")

        self.emp1= Employee("amirhosein", "sedaghati", 100000)
        self.emp2= Employee("skye", "beckham", 101000)


    def tearDown(self):
        print('tearDown \n')


    def test_email(self):
        print("test_email")

        self.assertEqual(self.emp1.email, "amirhosein.sedaghati@gmail.com")
        self.assertEqual(self.emp2.email, "skye.beckham@gmail.com")

        self.emp1.first= "sina"
        self.emp2.first= "david"

        self.assertEqual(self.emp1.email, "sina.sedaghati@gmail.com")
        self.assertEqual(self.emp2.email, "david.beckham@gmail.com")


    def test_fullName(self):
        print("test_fullName")

        self.assertEqual(self.emp1.fullName, "amirhosein sedaghati")
        self.assertEqual(self.emp2.fullName, "skye beckham")

        self.emp1.first= "sina"
        self.emp2.first= "david"

        self.assertEqual(self.emp1.fullName, "sina sedaghati")
        self.assertEqual(self.emp2.fullName, "david beckham")


    def test_apply_raise(self):
        print('test_apply_raise')

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 105000)
        self.assertEqual(self.emp2.pay, 106050)


    def test_monthly_schedule(self):
        print('test_monthly_schedule')

        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok= True
            mocked_get.return_value.text= 'success'

            employee_schedule= self.emp1.monthly_schedule("april")
            mocked_get.assert_called_with("http://www.company.com/sedaghati/april")
            self.assertEqual(employee_schedule, 'success')

            #----------------
            mocked_get.return_value.ok= False

            employee_schedule= self.emp2.monthly_schedule("june")
            mocked_get.assert_called_with("http://www.company.com/beckham/june")
            self.assertEqual(employee_schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()