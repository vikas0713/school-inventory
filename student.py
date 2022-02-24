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
            2: self.add,
            5: self.associate_standard,
            6: self.get_student_by_standard
        }

    def display_options(self):
        """All the display options for student table"""
        print("1. See List of students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Update standard of student")
        print("6. Get Student BY Standard")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            name = input("Enter Student name: ")
            self.student_option_map().get(selected_input)(name)
        elif selected_input == 5:
            standard_id = int(input("Enter the standard id: "))
            student_id = int(input("Enter the student id: "))
            self.student_option_map().get(selected_input)(standard_id, student_id)
        elif selected_input == 6:
            standard_id = int(input("Enter the standard id: "))
            self.student_option_map().get(selected_input)(standard_id)
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

    def associate_standard(self, standard_id, student_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {self.table} SET standard_id={standard_id} WHERE id={student_id}"
        )
        connection.commit()
        connection.close()
        print("Successfully updated record")

    def get_student_by_standard(self, standard_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE standard_id={standard_id}")
        for student in cursor.fetchall():
            print(student[1])
        connection.commit()
        connection.close()
        print("Successfully updated record")
