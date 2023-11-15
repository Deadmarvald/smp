from generator3D import *
from services import FileService

def input_mark():
    while True:
        mark = input("Please input a mark for the shape: ")
        if not AbstractShape.valid_mark(mark):
            print("Only one mark is required!")
        else:
            return mark

def select_color_code():
    while True:
        try:
            color_code = int(input("Select a color code: "))
            if color_code not in palette.keys():
                print("Select a valid color code!")
            else:
                return color_code
        except ValueError:
            print("A numeric value is required!")

def input_edge_length():
    while True:
        try:
            edge_length = int(input("Input the edge length: "))
            if edge_length <= 0:
                print("Edge length must be greater than zero!")
            else:
                return edge_length
        except ValueError:
            print("A numeric value is required!")

def input_scaling():
    while True:
        try:
            scaling = float(input("Set the scale: "))
            if scaling <= 0:
                print("Scale must be greater than zero!")
            else:
                return scaling
        except ValueError:
            print("A numeric value is required!")

file_2d = "2D.txt"
file_3d = "3D.txt"

def main():
    shape_created = False
    two_d_ready = False
    three_d_ready = False

    while True:
        print("Options:")
        print("1 - Generate a Square")
        print("2 - Show 2D")
        print("3 - Show 3D")
        print("4 - Save 2D")
        print("5 - Save 3D")
        print("0 - Quit")
        user_choice = input("What your choice?: ")

        match user_choice:
            case "1":
                mark = input_mark()
                print("Available colors:")
                show_palette()
                color_code = select_color_code()
                edge_length = input_edge_length()
                scaling = input_scaling()
                try:
                    shape = Square(edge_length, mark, color_code)
                    shape_created = True
                except ValueError as error:
                    print(error)
                    shape_created = False
            case "2":
                if shape_created:
                    representation_2D = shape.draw_2d()
                    for line in representation_2D:
                        print(line)
                    two_d_ready = True
                else:
                    print("No shape created yet!")
            case "3":
                if shape_created:
                    representation_3D = shape.draw_3d(scaling)
                    print(representation_3D)
                    three_d_ready = True
                else:
                    print("No shape created yet!")
            case "4":
                if two_d_ready:
                    try:
                        FileService.write_into_file(file_2d, "".join(representation_3D))
                    except PermissionError:
                        print("Insufficient permissions to write to file!")
                    except FileNotFoundError:
                        print("File not found!")
                else:
                    print("No shape created yet!")
            case "5":
                if three_d_ready:
                    try:
                        FileService.write_into_file(file_3d, representation_3D)
                    except PermissionError:
                        print("Insufficient permissions to write to file!")
                    except FileNotFoundError:
                        print("File not found!")
                else:
                    print("No shape created yet!")
            case "0":
                break
            case _:
                print("Please select a valid option!")

if __name__ == "__main__":
    main()