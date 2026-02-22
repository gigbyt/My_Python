class Student:
    def __init__(self, name, grade, section, roll_number):
        self.name = name
        self.grade = grade
        self.section = section
        self.roll_number = roll_number


students = []


while True:
    name = input("What is your name: ")
    grade = input("What is your grade: ")
    section = input("What is your section: ")
    roll_number = input("What is your Roll number: ")

    
    students.append(Student(name, grade, section, roll_number))

    
    more = input("Do you want to add another student? (yes/no): ").strip().lower()
    if more != 'yes':
        break


for student in students:
    print(f"Hello {student.name}, welcome to grade {student.grade}, section {student.section}!")


