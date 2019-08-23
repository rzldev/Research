
## Unit Testing supports test automation, sharing of setup and shutdown code for tests,
# aggregation of tests into collections, and independence of the tests from the reporting framework

## Import all the library needed
import unittest
from unittest.mock import patch
import Calc as c
from additionals.EmployeeTest import Employee as e

# patch() is a decorator that handles patching module and class level attributes within the scope of a test,
# along with sentinel for creating unique objects

## Create a test class
class TestCalc(unittest.TestCase) :
    # First Test
    def test_add(self) :
        result = c.add(10, 5)
        self.assertEqual(result, 15)

## Try to run multiple unit test
class TestCalcNew(unittest.TestCase) :
    # Second Test
    def testAdd(self) :
        self.assertEqual(c.add(3, 4), 7)
        self.assertEqual(c.add(-1, 1), 0)
        self.assertEqual(c.add(-2, 0), -2)

    # Third Test
    def testSub(self) :
        self.assertEqual(c.subtract(3, 4), -1)
        self.assertEqual(c.subtract(-1, 1), -2)
        self.assertEqual(c.subtract(-2, 0), -2)

    # Forth Test
    def testMul(self) :
        self.assertEqual(c.multiply(3, 4), 12)
        self.assertEqual(c.multiply(-1, 1), -1)
        self.assertEqual(c.multiply(-2, 0), 0)

    # Fifth Test
    def testDiv(self) :
        self.assertEqual(c.divide(3, 4), 3/4)
        self.assertEqual(c.divide(-1, 1), -1)

        self.assertRaises(ValueError, c.divide, -2, 0)
        #or
        with self.assertRaises(ValueError) :
            c.divide(-2, 0)

## Create a employee unit test class

class TestEmployee(unittest.TestCase) :

    # setUpClass is a class method which called before tests in an individual class are run
    @classmethod
    def setUpClass(cls) :
        pass

    # tearDownClass is a class method which called after tests in an individual class have run
    @classmethod
    def tearDownClass(cls) :
        pass

    # setUp Method called to prepare the test fixture. This is called immediately before calling the test method
    def setUp(self) :
        self.emp1 = e('Bruce', 'Wayne', 1000000)
        self.emp2 = e('Clark', 'Kent', 10000)

    # tearDown Method called immediately after the test method has been called and the result recorded
    def tearDown(self) :
        pass

    # email test
    def test_email(self) :
        self.assertEqual(self.emp1.email, 'Bruce.Wayne@gmail.com')
        self.assertEqual(self.emp2.email, 'Clark.Kent@gmail.com')

        self.emp1.last = 'Martha'
        self.emp2.last = 'Martha'

        self.assertEqual(self.emp1.email, 'Bruce.Martha@gmail.com')
        self.assertEqual(self.emp2.email, 'Clark.Martha@gmail.com')

    # full_name test
    def test_full_name(self) :
        self.assertEqual(self.emp1.full_name, 'Bruce Wayne')
        self.assertEqual(self.emp2.full_name, 'Clark Kent')

        self.emp1.last = 'Martha'
        self.emp2.last = 'Martha'

        self.assertEqual(self.emp1.full_name, 'Bruce Martha')
        self.assertEqual(self.emp2.full_name, 'Clark Martha')

    # salary test
    def test_salary(self) :
        self.emp1.apply_amount()
        self.emp2.apply_amount()

        self.assertEqual(self.emp1.salary, 1000000 * 1.07)
        self.assertEqual(self.emp2.salary, 10000 * 1.07)

    ## Introduction of mocking
    ## Mocking >> A mock object substitutes and imitates a real object within a testing environment
    def test_monthly_schedule(self) :
        with patch('additionals.EmployeeTest.requests.get') as mocked_get :
            # Create a success mock
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            # run mock
            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with("http://company.com/Wayne/May")
            self.assertEqual(schedule, "Success")

            # Create a bad response mock
            mocked_get.return_value.ok = False

            # run mock
            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with("http://company.com/Kent/June")
            self.assertEqual(schedule, "Bad Response!")

## Run the script
# We can run the script by typing this code in terminal
# python3 -m unittest UnitTest.py

# or add this code inside the script then run it normally
if __name__ == '__main__' :
    unittest.main()
