class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []  
        self.marks = []    

    def add_subject_marks(self, subject, marks):
        self.subjects.append(subject)
        self.marks.append(marks)

    def has_passed(self):
        total_marks = sum(self.marks)
        total_percentage = (total_marks / (len(self.subjects) * 100)) * 100
        subject_pass = all(mark >= 33 for mark in self.marks)
        total_pass = total_percentage >= 40
        return subject_pass and total_pass

f = open("text.txt", "w")
name = input("Enter your name: ")
student = Student(name)
subjects = ["Physics", "Maths", "Chemistry"]

for subject in subjects:
    marks = int(input(f"Enter your marks for {subject}: "))
    student.add_subject_marks(subject, marks)

if student.has_passed():
    print(f"Congratulations {student.name}, you have passed!")
else:
    print(f"Sorry {student.name}, you have failed.")
