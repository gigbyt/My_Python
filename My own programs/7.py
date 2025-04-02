class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def calculate_percentage(self):
        total_marks = sum(self.marks.values())
        percentage = (total_marks / (len(self.marks)*100))*100  
        return percentage
    def calculate_cgpa(self):
        total_marks = sum(self.marks.values())
        cgpa = total_marks / (len(self.marks)*10)    
        return cgpa
def store_students_details():
    students = {}
    while True:
        name = input("Enter students name (Type 'exit' to stop): ")
        if name.lower == 'exit':
            break
        roll_number = input("Enter Students Roll number: ")
        marks = {}
        for subject in ["Maths", "Science", "English"]:
            marks[subject] = int(input(f"Enter marks for {subject}: "))
            students[roll_number] = Student(name, roll_number, marks)
        return students
def generate_report_card(students):
    roll_number = input("Enter roll number of the student for the report card: ")
    if roll_number in students:
        student = students[roll_number]
        percentage = student.calculate_percentage()
        cgpa = student.calculate_cgpa()
        print("\nReport Card:")
        print(f"Name: {student.name}")
        print(f"Roll number: {student.roll_number}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"CGPA: {cgpa:.2f}")
    else:
        print("Student not found.")
def fetch_student_details(students):
    roll_number = input("Enter the roll number of the student to fetch details: ")
    if roll_number in students:
        student = students[roll_number]
        print("\nStudent Details: ")
        print(f"Name: {student.name}")
        print(f"Roll number: {student.roll_number}")
        print("Marks: ")
        for subject, marks in student.marks.items():
            print(f" {subject}:{marks}")
    else:
        print("Student not found.")
def display_final_results(students):
    for roll_number, student in students.items():
        percentage = student.calculate_percentage()
        print(f"Roll number : {roll_number}, Percentage : {percentage:.2f}%")
def check_scholarship(students):
    roll_number = input("ENter the the roll number of the student to fetch details: ")
    if roll_number in students:
        percentage = students[roll_number].calculate_percentage()
        if percentage >= 90:
            print("Congratulations! The student is eligible for the scholarship.")
        else:
            print("The student is not eligible for the scholarship.")
    else:
        print("Student not found")
student_data  = store_students_details()
generate_report_card(student_data)
fetch_student_details(student_data)
display_final_results(student_data)
check_scholarship(student_data)