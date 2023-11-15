import functions

if __name__ == '__main__':
    while True:
        try:
            while True:
                initial_text = input("Введіть слово, яке ви хочете перетворити в ASCII-арт: ")
                if not initial_text.isascii():
                    print("Текст повинен містити лише символи ASCII")
                    continue
                else:
                    break

            functions.display_fonts()
            font_position = int(input("Введіть номер шрифту, який ви хочете використовувати: "))
            if font_position not in functions.fonts:
                print("Невірний номер шрифту. Будь ласка, введіть ще раз.")
                continue

            functions.display_colors()
            color_position = int(input("Введіть номер кольору, який ви хочете використовувати: "))
            if color_position not in functions.colors:
                print("Невірний номер кольору. Будь ласка, введіть ще раз.")
                continue

        except ValueError as e:
            print("Будь ласка, введіть число.")
            continue

        while True:
            try:
                width = int(input("Введіть ширину тексту, яку ви хочете використовувати: "))
                if width <= 0:
                    print("Ширина повинна бути позитивним числом.")
                else:
                    break
            except ValueError as e:
                print("Будь ласка, введіть коректну ширину")

        modified_text = functions.get_text(initial_text, functions.fonts[font_position], color_position, width)
        print("ASCII-арт: ")
        print(modified_text)

        save_to_file = input("Зберегти текст у файл? (y/n): ").lower()
        if save_to_file == "y":
            filename = input("Введіть ім'я файлу для збереження тексту: ")
            functions.write_in_file(filename, modified_text)
            print(f"Текст збережено у файлі {filename}")

        continue_writing = input("Продовжити писати? (y/n): ").lower()
        if continue_writing != "y":
            break