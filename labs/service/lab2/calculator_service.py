import math


class CalculatorService:

    def __init__(self):
        self.__first_value = None
        self.__operator = None
        self.__second_value = None

    def input_values(self):
        try:
            self.__first_value = float(input("Enter the first value: "))
            self.__operator = str(input("Enter the operator ['+', '-', '*', '/', '**', '√', "
                                        "'%']: "))
            if self.__is_operator_correct(self.__operator):
                if self.__operator != "√":
                    self.__second_value = float(input("Enter the second value: "))
            else:
                raise RuntimeWarning("The input operator is incorrect")
        except ValueError as e:
            raise type(e)("The format of the number is invalid")

    @staticmethod
    def __is_operator_correct(operator):
        valid_operators = ('+', '-', '*', '/', '**', '√', '%')
        return operator in valid_operators

    def calculate(self):
        result = 0  # Initialize result to handle the "%"

        if self.__operator == "+":
            result = self.__first_value + self.__second_value
        elif self.__operator == "-":
            result = self.__first_value - self.__second_value
        elif self.__operator == "*":
            result = self.__first_value * self.__second_value
        elif self.__operator == "/":
            if self.__second_value == 0:
                raise ZeroDivisionError("Impossible to divide")
            result = self.__first_value / self.__second_value
        elif self.__operator == "**":
            result = self.__first_value ** self.__second_value
        elif self.__operator == "√":
            if self.__first_value < 0:
                raise ArithmeticError("Number is negative, therefore it is impossible "
                                      "to calculate the square root")
            result = math.sqrt(self.__first_value)
        elif self.__operator == "%":
            result = self.__first_value % self.__second_value

        return result

    def __str__(self):
        return f"CalculatorService: first_value={self.__first_value}, operator={self.__operator}," \
               f"second_value={self.__second_value}"
