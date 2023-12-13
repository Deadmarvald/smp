import unittest
from service.lab2.calculator_service import CalculatorService  # Replace 'your_module' with the actual module name

class TestCalculatorService(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorService()

    def test_addition(self):
        self.calculator._CalculatorService__first_value = 3.5
        self.calculator._CalculatorService__second_value = 2
        self.calculator._CalculatorService__operator = '+'
        self.assertAlmostEqual(self.calculator.calculate(), 5.5)

    def test_subtraction(self):
        self.calculator._CalculatorService__first_value = 5
        self.calculator._CalculatorService__second_value = 3
        self.calculator._CalculatorService__operator = '-'
        self.assertAlmostEqual(self.calculator.calculate(), 2)

    def test_multiplication(self):
        self.calculator._CalculatorService__first_value = 6
        self.calculator._CalculatorService__second_value = 7
        self.calculator._CalculatorService__operator = '*'
        self.assertAlmostEqual(self.calculator.calculate(), 42)

    def test_division(self):
        self.calculator._CalculatorService__first_value = 15
        self.calculator._CalculatorService__second_value = 3
        self.calculator._CalculatorService__operator = '/'
        self.assertAlmostEqual(self.calculator.calculate(), 5)

    def test_division_by_zero(self):
        self.calculator._CalculatorService__first_value = 5
        self.calculator._CalculatorService__second_value = 0
        self.calculator._CalculatorService__operator = '/'
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate()

    def test_square_root(self):
        self.calculator._CalculatorService__first_value = 9
        self.calculator._CalculatorService__operator = '√'
        self.assertAlmostEqual(self.calculator.calculate(), 3)

    def test_square_root_negative(self):
        self.calculator._CalculatorService__first_value = -9
        self.calculator._CalculatorService__operator = '√'
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate()


if __name__ == '__main__':
    unittest.main()
