#!/usr/bin/env python3
import unittest
from tests.pages.Calc import Calculator
from  appium  import  webdriver


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        run_locally = False
        url = 'http://localhost:4723/wd/hub'
        desired_caps = {}
        if run_locally:
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['app'] = '/Users/qubilearnd/Work/apks/Calculator.apk'

        self.driver = webdriver.Remote(url, desired_caps)
        self.calculator = Calculator(self.driver)

    def test_sum_numbers(self):    
        self.calculator.sum(1, 2, 3)

    def test_sum_floats(self):
        self.calculator.sum(1.5, 2, .5)

    def test_multiply_numbers(self):    
        self.calculator.multiplying(2, 4)

    def test_multiply_floats(self):
        self.calculator.multiplying(2.5, 2)

    def test_divide_numbers(self):    
        self.calculator.dividing(4, 2)

    def test_divide_floats(self):
        self.calculator.dividing(4.5, 2)

    def tearDown(self):
        self.driver.quit()


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()
