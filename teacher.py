"""
Teacher related CRUD operations are written in this file
"""


class Teacher:
    """Utility for teacher table"""
    def __init__(self):
        pass

    @staticmethod
    def display_options():
        """All the display options for student table"""
        print("1. See List of Teachers")
        print("2. Add Teacher")
        print("3. Update Teacher")
        print("4. Delete Teacher")
