class Calculator:
    def __init__(self, decimal=2, max_history_size=10):
        self.memory = []
        self.history = []
        self.decimal = decimal
        self.max_history_size = max_history_size
        self.result = 0 
        self.num1 = 0
        self.operator = '';
        self.num2 = 0  

    def run(self):
        while True:
            try:
                self.show_menu()
                choice = input("Ваш вибір: ").lower()

                if choice == 'k':
                    self.calculate()
                elif choice == 'h':
                    self.display_history()
                elif choice == 'r':
                    self.display_memory()
                else:
                    self.calculate()
                    
                self.save_result()
                self.update_history()
                
            except ValueError as e:
                print(f"Помилка: {e}")
            except ZeroDivisionError as e:
                print(f"Помилка: {e}")

            another_calculation = input("Бажаєте виконати ще одне обчислення? (y/n): ")
            if another_calculation.lower() != 'y':
                break

    def show_menu(self):
        print("\nМеню:")
        print("R - Відновлення результату")
        print("H - Історія обчислень")
        print("K - Використати калькулятор")

    def calculate(self):
        self.num1 = float(input("Введіть перше число: "))
        self.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

        if self.operator not in ['+', '-', '*', '/', '^', '√', '%']:
            raise ValueError("Недійсний оператор. Введіть один із +, -, *, /, ^, √, %")

        if self.operator != '√':
            self.num2 = float(input("Введіть друге число: "))

        result = 0

        if self.operator == '+':
            result = self.num1 + self.num2
        elif self.operator == '-':
            result = self.num1 - self.num2
        elif self.operator == '*':
            result = self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 == 0:
                raise ZeroDivisionError("Ділення на нуль недопустимо.")
            result = self.num1 / self.num2
        elif self.operator == '^':
            result = self.num1 ** self.num2
        elif self.operator == '√':
            result = self.num1 ** 0.5
        elif self.operator == '%':
            result = self.num1 % self.num2

        result = round(result, self.decimal)
        print(f"Результат: {result}")
        self.result = result

    def save_result(self):
        save_operator = input("Хочете зберегти результат? (y/n): ").lower()
        if save_operator == 'y':
            self.memory.append(f"{self.num1} {self.operator} {self.num2} = {self.result}")

    def display_memory(self):
        print("\nЗбережені обчислення:")
        for item in self.memory:
            print(item)

    def display_history(self):
        print("\nІсторія обчислень:")
        for item in self.history:
            print(item)

    def update_history(self):
        if len(self.history) >= self.max_history_size:
            del self.history[0]

        self.history.append(f"{self.num1} {self.operator} {self.num2} = {self.result}")


if __name__ == "__main__":
    decimal = int(input("Введіть скільки десяткових розрядів після коми показувати: "))
    max_history_size = int(input("Введіть скільки обчислень зберігати у історії: "))

    calculator = Calculator(decimal, max_history_size)
    calculator.run()
