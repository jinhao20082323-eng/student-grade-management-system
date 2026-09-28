import matplotlib.pyplot as plt
from student import Student
# Letter Grading system
students = []
def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(subject + " Grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def save_students():
    with open("data.txt", "w") as file:
        for student in students:
            file.write(f'{student.name},{student.math_grade},{student.english_grade},{student.science_grade}\n')
    print("Data saved.")
def load_students():
    try:
        with open("data.txt", "r") as file:

            for line in file:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                data = line.split(",")

                # Check data format
                if len(data) != 4:
                    print("Warning: Invalid data format skipped.")
                    continue

                name = data[0]

                # Check whether grades are numbers
                try:
                    math_grade = float(data[1])
                    english_grade = float(data[2])
                    science_grade = float(data[3])

                except ValueError:
                    print(
                        f'Warning: Invalid student "{name}" data skipped.'
                    )
                    continue

                # Check grade range
                if not (
                    0 <= math_grade <= 100
                    and 0 <= english_grade <= 100
                    and 0 <= science_grade <= 100
                ):
                    print(
                        f'Warning: Student "{name}" has invalid grades, data skipped.'
                    )
                    continue

                # Create Student object
                students.append(
                    Student(
                        name,
                        math_grade,
                        english_grade,
                        science_grade
                    )
                )

    except FileNotFoundError:
        pass
def delete_all():
    confirm = input("Are you sure you want to delete all data? Enter Y to confirm: ")
    if confirm.upper() == "Y":
        students.clear()
        save_students()
        print("Data deleted.")
    else:
        print("Delete cancelled.")
def add_student():
    name = input("Enter student name: ")
    math_grade = get_valid_grade("Math")
    english_grade = get_valid_grade("English")
    science_grade = get_valid_grade("Science")
    students.append(
        Student(
            name,
            math_grade,
            english_grade,
            science_grade
        )
    )
    save_students()
    print("Student added successfully.")
def view_student():
    if not students:
        print("Student dataset is empty.")
    else:
        print("\nStudent Results")
        for student in students:
            print(
                student.name,
                "-",
                round(student.calculate_average(), 2),
                "-",
                get_grade(student.calculate_average())
            )
def search_student():
    if not students:
        print("Student dataset is empty.")
    else:
        search_name = input("Enter student name: ")
        found = False
        for student in students:
            if search_name.lower() in student.name.lower():
                print(
                    student.name,
                    "-",
                    round(student.calculate_average(), 2),
                    "-",
                    get_grade(student.calculate_average())
                )
                found = True
        if not found:
            print("Student not found.")
def edit_student():
    if not students:
        print("Student dataset is empty.")
    else:
        edit_name = input("Enter student name: ")
        found = False
        for student in students:
            if student.name.lower() == edit_name.lower():
                student.math_grade = get_valid_grade("Math")
                student.english_grade = get_valid_grade("English")
                student.science_grade = get_valid_grade("Science")
                save_students()
                print("Student updated.")
                found = True
                break
        if not found:
            print("Student not found.")
def delete_student():
    if not students:
        print("Student dataset is empty.")
    else:
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
def ranking():
    if not students:
        print("Student dataset is empty.")
    else:
        sorted_students = sorted(
            students,
            key=lambda x: x.calculate_average(),
            reverse=True
        )
        rank = 1
        for student in sorted_students:
            print(rank,": ",student.name,"-",round(student.calculate_average(), 2),"-",get_grade(student.calculate_average()))
            rank += 1
def statistics():
    if not students:
        print("Student dataset is empty.")
    else:
        highest = max(students, key=lambda x: x.calculate_average())

        lowest = min(students, key=lambda x: x.calculate_average())

        class_average = (
                sum(student.calculate_average() for student in students)
                / len(students)
            )
        print("\n===== STATISTICS =====")
        print("Total Students:", len(students))
        print("Highest Score:", highest.name, round(highest.calculate_average(), 2))
        print("Lowest Score:", lowest.name, round(lowest.calculate_average(), 2))
        print("Class Average:", round(class_average, 2))
def grade_chart():
    if not students:
        print("Student dataset is empty.")
    else:
        names = [student.name for student in students]
        averages = [student.calculate_average() for student in students]
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

print("Student Grade Management System")


load_students()

print("Data loaded successfully.")
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
    print("10. Delete all data")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        ranking()
    elif choice == "7":
        save_students()
        print("Goodbye!")
        break
    elif choice == "8":
        statistics()
    elif choice == "9":
        grade_chart()
    elif choice == "10":
        delete_all()
    else:
        print("Please enter a number from the menu.")