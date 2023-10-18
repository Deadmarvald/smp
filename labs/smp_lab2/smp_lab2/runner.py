from calculator import Calculator
from console_output import ConsoleOutput

if __name__ == "__main__":
    decimal = int(ConsoleOutput.get_user_input("Введіть скільки десяткових розрядів після коми показувати: "))
    max_history_size = int(ConsoleOutput.get_user_input("Введіть скільки обчислень зберігати у історії: "))

    calculator = Calculator(decimal, max_history_size)

    while True:
        try:
            ConsoleOutput.show_message("\nМеню:")
            ConsoleOutput.show_message("R - Відновлення результату")
            ConsoleOutput.show_message("H - Історія обчислень")
            ConsoleOutput.show_message("K - Використати калькулятор")

            choice = ConsoleOutput.get_user_input("Ваш вибір: ").lower()

            if choice == 'k':
                num1 = float(ConsoleOutput.get_user_input("Введіть перше число: "))
                operator = ConsoleOutput.get_user_input("Введіть оператор (+, -, *, /, ^, √, %): ")

                if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                    raise ValueError("Недійсний оператор. Введіть один із +, -, *, /, ^, √, %")

                if operator != '√':
                    num2 = float(ConsoleOutput.get_user_input("Введіть друге число: "))
                    result = calculator.calculate(num1, operator, num2)
                else:
                    result = calculator.calculate(num1, operator, 0)

                ConsoleOutput.show_message(f"Результат: {result}")

                save_quest = ConsoleOutput.get_user_input("Хочете зберегти результат?(y/n): ").lower()
                if save_quest == 'y':
                    calculator.save_result(num1, operator, num2, result)

            elif choice == 'h':
                ConsoleOutput.show_message("\nІсторія обчислень:")
                for item in calculator.display_history():
                    ConsoleOutput.show_message(item)

            elif choice == 'r':
                ConsoleOutput.show_message("\nЗбережені обчислення:")
                for item in calculator.display_memory():
                    ConsoleOutput.show_message(item)

        except ValueError as e:
            ConsoleOutput.show_message(f"Помилка: {e}")
        except ZeroDivisionError as e:
            ConsoleOutput.show_message(f"Помилка: {e}")

        another_calculation = ConsoleOutput.get_user_input("Бажаєте виконати ще одне обчислення? (y/n): ")
        if another_calculation.lower() != 'y':
            break