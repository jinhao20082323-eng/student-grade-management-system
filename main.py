from student import Student
# Letter Grading system
def get_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    else:
        return "F"

print("Student Grade Management System")

students = []
# Get the info of 3 students
for i in range(3):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    math_grade = float(input("Math Grade: "))
    english_grade = float(input("English Grade: "))
    science_grade = float(input("Science Grade: "))

    average = (math_grade + english_grade + science_grade) / 3

    students.append(Student(name, average))
# Show results w/ rank
print("\nStudent Results")

for student in students:
    print(student.name,
        "-",
        round(student.average, 2),
        "-",
        get_grade(student.average))
students.sort(
    key=lambda x: x.average,
    reverse=True
)

print("\nRanking")

rank = 1

for student in students:
    print(rank,
          student.name,
          "-",
          round(student.average, 2),
          "-",
          get_grade(student.average))

    rank += 1
# menu system
while True:

    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. Delete Student")
    print("6. Ranking")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "2":

        print("\nStudent Results")

        for student in students:

            print(
                student.name,
                "-",
                round(student.average, 2),
                "-",
                get_grade(student.average)
            )
    elif choice == "1":

        name = input("Enter student name: ")

        math_grade = float(input("Math Grade: "))
        english_grade = float(input("English Grade: "))
        science_grade = float(input("Science Grade: "))

        average = (
            math_grade +
            english_grade +
            science_grade
        ) / 3

        students.append(
            Student(name, average)
        )

        print("Student added successfully.")
    elif choice == "3":

        search_name = input("Enter student name: ")

        found = False

        for student in students:

            if student.name.lower() == search_name.lower():

                print(
                    student.name,
                    "-",
                    round(student.average, 2),
                    "-",
                    get_grade(student.average)
                )

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":

        edit_name = input("Enter student name: ")

        found = False

        for student in students:

            if student.name.lower() == edit_name.lower():

                new_average = float(
                    input("Enter new average: ")
                )

                student.average = new_average

                print("Student updated.")

                found = True

                break

        if not found:
            print("Student not found.")

    elif choice == "5":

        delete_name = input("Enter student name: ")

        found = False

        for student in students:

            if student.name.lower() == delete_name.lower():

                students.remove(student)

                print("Student deleted.")

                found = True

                break

        if not found:
            print("Student not found.")

    elif choice == "6":

        students.sort(
            key=lambda x: x.average,
            reverse=True
        )

        rank = 1

        for student in students:

            print(
                rank,
                student.name,
                "-",
                round(student.average, 2),
                "-",
                get_grade(student.average)
            )

            rank += 1

    elif choice == "7":
        print("Goodbye!")
        break