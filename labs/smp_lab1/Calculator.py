import math

def show_menu():
    print("\nМеню:")
    print("R - Відновлення результату")
    print("H - Історія обчислень")
    print("K - Використати калькулятор")

def calculate(num1, operator, num2, decimal):
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '^':
        result = raise_to_a_power(num1, num2)
    elif operator == '√':
        result = compute_square_root(num1)
    elif operator == '%':
        result = divide_by_modulo(num1, num2)
    else:
        raise ValueError("Недійсний оператор")

    return round(result, decimal)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Ділення на нуль недопустимо")
    return num1 / num2

def raise_to_a_power(num1, num2):
    return num1 ** num2

def compute_square_root(num):
    if num < 0:
        raise ArithmeticError("Number is negative, therefore it is impossible to calculate the square root")
    return math.sqrt(num)

def divide_by_modulo(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Ділення на нуль недопустимо")
    return num1 % num2

def run_calculator(decimal, max_history_size):
    memory = []
    history = []
    while True:
        show_menu()
        choice = input("Ваш вибір: ").lower()

        if choice in ['k', 'r', 'h']:
            if choice == 'k':
                num1 = float(input("Введіть перше число: "))
                operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
                if operator != '√':
                    num2 = float(input("Введіть друге число: "))
                else:
                    num2 = 0
                result = calculate(num1, operator, num2, decimal)
                print(f"Результат: {result}")
                if len(history) >= max_history_size:
                    history.pop(0)
                history.append(f"{num1} {operator} {num2} = {result}")

                save_operator = input("Хочете зберегти результат? (y/n): ").lower()
                if save_operator == 'y':
                    memory.append(f"{num1} {operator} {num2} = {result}")

            elif choice == 'h':
                print("\nІсторія обчислень:")
                for item in history:
                    print(item)

            elif choice == 'r':
                print("\nЗбережені обчислення:")
                for item in memory:
                    print(item)

        another_calculation = input("Бажаєте виконати ще одне обчислення? (y/n): ")
        if another_calculation.lower() != 'y':
            break

if __name__ == "__main__":
    decimal = int(input("Введіть скільки десяткових розрядів після коми показувати: "))
    max_history_size = int(input("Введіть скільки обчислень зберігати у історії: "))

    run_calculator(decimal, max_history_size)