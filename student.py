"""
Student related CRUD operations are written in this file
"""
from config import get_db_cursor


class Student:
    """Student util to do db actions"""
    table = 'tb_students'

    def __init__(self):
        pass

    def student_option_map(self):
        return {
            1: self.get_list,
            2: self.add
        }

    def display_options(self):
        """All the display options for student table"""
        print("1. See List of students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            name = input("Enter Student name: ")
            self.student_option_map().get(selected_input)(name)
        else:
            self.student_option_map().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        for student in cursor.fetchall():
            print(f'{student[0]}---{student[1]}')
        connection.close()

    def add(self, name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table}(name) VALUES('{name}')")
        connection.commit()
        connection.close()
        print("Successfully added 1 record")
