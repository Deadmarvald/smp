import unittest
import smp_lab1.Calculator as calculator

class TestCalculator(unittest.TestCase):
    def test_basic_addition(self):
        self.assertAlmostEqual(calculator.add(3.5, 2), 5.5)
        self.assertAlmostEqual(calculator.add(-4, -6), -10)
        self.assertAlmostEqual(calculator.add(0, 0), 0)

    def test_addition_with_errors(self):
        with self.assertRaises(TypeError):
            calculator.add("hello", 2)
            calculator.add(2.5, "hello")

    def test_basic_subtraction(self):
        self.assertAlmostEqual(calculator.subtract(5, 3), 2)
        self.assertAlmostEqual(calculator.subtract(-7, -2), -5)
        self.assertAlmostEqual(calculator.subtract(8, 10), -2)

    def test_subtraction_with_errors(self):
        with self.assertRaises(TypeError):
            calculator.subtract("hello", 4)
            calculator.subtract(3.6, "hello")

    def test_basic_multiplication(self):
        self.assertAlmostEqual(calculator.multiply(6, 7), 42)
        self.assertAlmostEqual(calculator.multiply(-3, 4), -12)
        self.assertAlmostEqual(calculator.multiply(0, 5), 0)

    def test_multiplication_with_errors(self):
        with self.assertRaises(TypeError):
            calculator.multiply("hello", 8)
            calculator.multiply(3.14, "hello")

    def test_basic_division(self):
        self.assertAlmostEqual(calculator.divide(15, 3), 5)
        self.assertAlmostEqual(calculator.divide(-10, 5), -2)
        self.assertAlmostEqual(calculator.divide(5, 2), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)
            calculator.divide(-1, 0)

    def test_division_with_errors(self):
        with self.assertRaises(TypeError):
            calculator.divide("hello", 3)
            calculator.divide(7, "hello")

if __name__ == '__main__':
    unittest.main()