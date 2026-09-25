import matplotlib.pyplot as plt
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
def save_students():

    with open("data.txt", "w") as file:

        for student in students:

            file.write(
                student.name + "," +
                str(student.average) + "\n"
            )
    print("Data Saved.")
def load_students():

    try:

        with open("data.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 2:

                    name = data[0]
                    average = float(data[1])

                    students.append(
                        Student(name, average)
                    )

    except FileNotFoundError:

        pass
print("Student Grade Management System")

students = []

load_students()

print("Data loaded successfully.")
# Get the info of 3 students
# for i in range(3):

#     print("\nStudent", i + 1)

#     name = input("Enter student name: ")

#     math_grade = float(input("Math Grade: "))
#     english_grade = float(input("English Grade: "))
#     science_grade = float(input("Science Grade: "))

#     average = (math_grade + english_grade + science_grade) / 3

#     students.append(Student(name, average))
# Show results w/ rank

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
    print("8. Statistics")
    print("9. Grade Chart")
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
        save_students()
        print("Student added successfully.")
    elif choice == "3":

        search_name = input("Enter student name: ")

        found = False

        for student in students:

            if search_name.lower() in student.name.lower():

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

                math_grade = float(input("Math Grade: "))
                english_grade = float(input("English Grade: "))
                science_grade = float(input("Science Grade: "))

                new_average = (
                    math_grade +
                    english_grade +
                    science_grade
                ) / 3

                student.average = new_average
                save_students()
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
                save_students()
                print("Student deleted.")

                found = True

                break

        if not found:
            print("Student not found.")

    elif choice == "6":

        sorted_students = sorted(
            students,
            key=lambda x: x.average,
            reverse=True
        )

        rank = 1

        for student in sorted_students:

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
        save_students()
        print("Goodbye!")
        break
    elif choice == "8":

        if len(students) > 0:

            highest = max(students, key=lambda x: x.average)

            lowest = min(students, key=lambda x: x.average)

            class_average = (
                sum(student.average for student in students)
                / len(students)
            )
            print("\n===== STATISTICS =====")
            print("Total Students:", len(students))
            print("Highest Score:", highest.name, round(highest.average, 2))
            print("Lowest Score:", lowest.name, round(lowest.average, 2))
            print("Class Average:", round(class_average, 2))
        else:
            print("No students found.")
    elif choice == "9":

        if len(students) == 0:

            print("No students found.")

        else:

            names = [student.name for student in students]
            averages = [student.average for student in students]

            plt.figure(figsize=(8, 5))

            bars = plt.bar(names, averages)


            plt.title("Student Grade Chart")
            plt.xlabel("Students")
            plt.ylabel("Average Score")
            plt.ylim(0, 110)
            for bar, average in zip(bars, averages):
                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 1,
                    str(round(average, 2)),
                    ha="center"
                )

            plt.tight_layout()
            plt.savefig("grade_chart.png")

            print("Chart saved as grade_chart.png")