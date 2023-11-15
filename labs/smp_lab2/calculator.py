class Calculator:
    def __init__(self, decimal=2, max_history_size=10):
        self.memory = []
        self.history = []
        self.decimal = decimal
        self.max_history_size = max_history_size
        self.result = 0
        self.num1 = 0
        self.operator = ''
        self.num2 = 0

    def calculate(self, num1, operator, num2):
        result = 0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль недопустимо.")
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '√':
            result = num1 ** 0.5
        elif operator == '%':
            result = num1 % num2

        result = round(result, self.decimal)
        self.update_history(num1, operator, num2, result);
        return result

    def save_result(self, num1, operator, num2, result):
        self.memory.append(f"{num1} {operator} {num2} = {result}")

    def display_memory(self):
        return self.memory

    def display_history(self):
        return self.history

    def update_history(self, num1, operator, num2, result):
        if len(self.history) >= self.max_history_size:
            del self.history[0]

        self.history.append(f"{num1} {operator} {num2} = {result}")

