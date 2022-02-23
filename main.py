"""
Entrypoint for the project
"""
from standard import Standard
from student import Student
from teacher import Teacher

OPTION_MAP = {
    1: Student().display_options,
    2: Teacher.display_options,
    3: Standard.display_options
}


def display_options():
    """Options in the system"""
    print("Welcome to School Inventory System")
    print("Select your options")
    print("1. Student")
    print("2. Teacher")
    print("3. Standard")


def option_router():
    """routes option according to the input"""
    selected_option = int(input("Enter your option: "))
    return OPTION_MAP.get(selected_option)()


if __name__ == '__main__':
    display_options()
    option_router()
