# -*- coding: UTF-8 -*-
# ToolName   : /Student-Grading-System
# Author     : ScriptedByMark
# License    : MIT
# Language   : Python
# Env        : #!/usr/bin/env python3


class GradeSystem:
    def __init__(self):
        self.subjects = []  
        self.students = {}   

    def enter_subjects(self):
        print("--- Welcome to the Student Grading System ---")
        try:
            num_subjects = int(input("Enter number of subjects: "))
            for i in range(1, num_subjects + 1):
                subject_name = input(f"Enter subject {i}: ").strip()
                self.subjects.append(subject_name)
            print(f"\nSubjects added: {', '.join(self.subjects)}")
        except ValueError:
            print("Invalid input. Please enter a valid number of subjects.")

    def add_student(self):
        student_name = input("Enter student full name: ").strip()
        if student_name:
            self.students[student_name] = {subject: None for subject in self.subjects}
            print(f"Student '{student_name}' added.")
        else:
            print("Invalid input. Please enter a valid name.")

    def add_grades(self):
        student_name = input("Enter the student's full name to add grades: ").strip()
        if student_name in self.students:
            for subject in self.subjects:
                while True:
                    try:
                        grade = float(input(f"Enter grade for {subject}: "))
                        if 0 <= grade <= 100:
                            self.students[student_name][subject] = grade
                            break
                        else:
                            print("Please enter a grade between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a valid grade.")
            print(f"Grades added for {student_name}.")
        else:
            print("Student not found.")

    def calculate_average(self, student_name):
        if student_name in self.students:
            grades = [grade for grade in self.students[student_name].values() if grade is not None]
            if grades:
                avg_grade = sum(grades) / len(grades)
                return avg_grade
            else:
                print("No grades available to calculate average.")
        else:
            print("Student not found.")
        return None

    def display_students(self):
        if not self.students:
            print("No students to display.")
            return
        for student, grades in self.students.items():
            print(f"\nStudent: {student}")
            for subject, grade in grades.items():
                print(f"{subject}: {grade if grade is not None else 'No grade'}")
            avg_grade = self.calculate_average(student)
            if avg_grade is not None:
                print(f"Average Grade: {avg_grade:.2f}")

    def run(self):
        self.enter_subjects()
        while True:
            print("\nWhat do you want to do?")
            print("1. Add a student")
            print("2. Add grades for a student")
            print("3. Calculate average grade")
            print("4. Display all students and grades")
            print("5. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_grades()
            elif choice == '3':
                student_name = input("Enter the student's full name to calculate the average grade: ").strip()
                avg_grade = self.calculate_average(student_name)
                if avg_grade is not None:
                    print(f"Average Grade for {student_name}: {avg_grade:.2f}")
            elif choice == '4':
                self.display_students()
            elif choice == '5':
                print("--- THANK YOU! ---")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the Grade System
if __name__ == "__main__":
    system = GradeSystem()
    system.run()
