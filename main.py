from student import Student

print("Student Grade Management System")

students = []

for i in range(3):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    math_grade = float(input("Math Grade: "))
    english_grade = float(input("English Grade: "))
    science_grade = float(input("Science Grade: "))

    average = (math_grade + english_grade + science_grade) / 3

    students.append(Student(name, average))

print("\nStudent Results")

for student in students:
    print(student.name, "-", round(student.average, 2))

students.sort(
    key=lambda x: x.average,
    reverse=True
)

print("\nRanking")

rank = 1

for student in students:
    print(rank, student.name, "-", round(student.average, 2))
    rank += 1
