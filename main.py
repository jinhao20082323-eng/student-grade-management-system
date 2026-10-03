import csv
import matplotlib.pyplot as plt
from student import Student

students = []

def is_valid_grade(grade):
    return 0 <= grade <= 100


def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(subject + " Grade: "))
            if is_valid_grade(grade):
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
                if not line:
                    continue
                data = line.split(",")
                if len(data) != 4:
                    print("Warning: Invalid data format skipped.")
                    continue
                name = data[0].strip()
                if not name:
                    print("Warning: Empty name found.")
                    continue
                try:
                    math_grade = float(data[1])
                    english_grade = float(data[2])
                    science_grade = float(data[3])

                except ValueError:
                    print(
                        f'Warning: Invalid student "{name}" data skipped.'
                    )
                    continue
                if not all(is_valid_grade(grade) for grade in [math_grade, english_grade, science_grade]):
                    print(
                        f'Warning: Student "{name}" has invalid grades, data skipped.'
                    )
                    continue
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


def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Student name cannot be empty.")


def add_student():
    name = get_valid_name()
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
        return
    print("\nStudent Results")
    for student in students:
        average = student.calculate_average()
        print(f'{student.name}: {average:.2f} ({get_grade(average)})')


def search_student():
    if not students:
        print("Student dataset is empty.")
        return
    search_name = input("Enter student name: ").strip()
    found = False
    for student in students:
        if search_name.lower() in student.name.lower():
            average = student.calculate_average()
            print(f'{student.name}: {average:.2f} ({get_grade(average)})')
            found = True
    if not found:
        print("Student not found.")


def edit_student():
    if not students:
        print("Student dataset is empty.")
        return
    edit_name = input("Enter student name: ").strip()
    for student in students:
        if student.name.lower() == edit_name.lower():
            student.math_grade = get_valid_grade("Math")
            student.english_grade = get_valid_grade("English")
            student.science_grade = get_valid_grade("Science")
            save_students()
            print("Student updated.")
            return
    print("Student not found.")


def delete_student():
    if not students:
        print("Student dataset is empty.")
        return
    delete_name = input("Enter student name: ").strip()
    for student in students:
        if student.name.lower() == delete_name.lower():    
            students.remove(student)
            save_students()
            print("Student deleted.")   
            return   
    print("Student not found.")


def sort_students():
    if not students:
        print("Student dataset is empty.")
        return
    print("Sort by:",
    "1. Math Grade",
    "2. English Grade",
    "3. Science Grade",
    "4. Average",
    sep="\n"
    )
    while True:
        choice = input("Choose: ")
        if choice == "1":
            title = "Math"
            key = lambda x: x.math_grade
            break
        elif choice == "2":
            title = "English"
            key = lambda x: x.english_grade
            break
        elif choice == "3":
            title = "Science"
            key = lambda x: x.science_grade
            break
        elif choice == "4":
            title = "Average"
            key = lambda x: x.calculate_average()
            break
        else:
            print("Please choose a number from the menu.")
    print("Sort order:",
    "1. Highest to Lowest",
    "2. Lowest to Highest",
    sep="\n"
    )
    while True:
        choice = input("Choose: ")
        if choice in ["1", "2"]:
            break
        else:
            print("Please choose a number from the menu.")
    sorted_students = sorted(
    students,
    key=key,
    reverse=choice == "1"
    )
    print(f"Sorted by {title} Grade: ")
    for rank, student in enumerate(sorted_students, start=1):
        grade = key(student)
        print(f"{rank}. {student.name}: {grade:.2f} ({get_grade(grade)})")


def statistics():
    if not students:
        print("Student dataset is empty.")
        return
    math_average = sum(student.math_grade for student in students) / len(students)
    english_average = sum(student.english_grade for student in students) / len(students)
    science_average = sum(student.science_grade for student in students) / len(students)
    highest_math = max(students, key=lambda x: x.math_grade)
    highest_english = max(students, key=lambda x: x.english_grade)
    highest_science = max(students, key=lambda x: x.science_grade)
    highest_student = max(students, key=lambda x: x.calculate_average())
    lowest_student = min(students, key=lambda x: x.calculate_average())
    class_average = sum(student.calculate_average() for student in students) / len(students)
    failed = sum(student.calculate_average() < 60 for student in students)
    passed = len(students) - failed
    pass_rate = passed / len(students) * 100
    print("\n===== STATISTICS =====")
    print(f'Total Students: {len(students)}\n')
    print(f'Math Average: {math_average:.2f}')
    print(f'English Average: {english_average:.2f}')
    print(f'Science Average: {science_average:.2f}')
    print(f'Class Average: {class_average:.2f}')
    print(f'Highest in Math: {highest_math.name} ({highest_math.math_grade:.2f})')
    print(f'Highest in English: {highest_english.name} ({highest_english.english_grade:.2f})')
    print(f'Highest in Science: {highest_science.name} ({highest_science.science_grade:.2f})')
    print(f'Highest Score: {highest_student.name} ({highest_student.calculate_average():.2f})')
    print(f'Lowest Score: {lowest_student.name} ({lowest_student.calculate_average():.2f})')
    print(f'Passed: {passed}\nFailed: {failed}\nPass rate: {pass_rate:.2f}%')


def add_bar_labels(bars, grades):
    for bar, grade in zip(bars, grades):
        if int(grade) == grade:
            grade = int(grade)
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            str(round(grade, 2)),
            ha="center",
            fontsize=8
        )


def grade_chart():
    if not students:
        print("Student dataset is empty.")
        return
    names = [student.name for student in students]
    math_grades = [student.math_grade for student in students]
    english_grades = [student.english_grade for student in students]
    science_grades = [student.science_grade for student in students]
    averages = [student.calculate_average() for student in students]
    x = range(len(students))
    width = 0.2
    plt.figure(figsize=(10, 7))
    bars = [plt.bar(
        [position - 1.5 * width for position in x],
        math_grades,
        width=width,
        label="Math"
    ),
    plt.bar(
        [position - 0.5 * width for position in x],
        english_grades,
        width=width,
        label="English"
    ),
    plt.bar(
        [position + 0.5 * width for position in x],
        science_grades,
        width=width,
        label="Science"
    ),
    plt.bar(
        [position + 1.5 * width for position in x],
        averages,
        width=width,
        label="Average"
    )]
    grades = [math_grades, english_grades, science_grades, averages]
    plt.title("Student Grade Chart")
    plt.xlabel("Students")
    plt.xticks(x, names)
    plt.axhline(y=60, label="Pass Line (60)", linestyle="--", color="black")
    plt.ylabel("Score")
    plt.ylim(0, 110)
    for bar_group, grade_group in zip(bars, grades):
        add_bar_labels(bar_group, grade_group)
    plt.legend()    
    plt.tight_layout()
    plt.savefig("grade_chart.png")
    print("Chart saved as grade_chart.png")


def view_student_details():
    if not students:
        print("Student dataset is empty.")
        return
    name = input("Enter student name: ").strip()
    found = False
    for student in students:
        if name.lower() in student.name.lower():
            average = student.calculate_average()
            print(f"\n{student.name}",
            f"Math Grade: {student.math_grade}",
            f"English Grade: {student.english_grade}",
            f"Science Grade: {student.science_grade}",
            f"Average: {average:.2f} ({get_grade(average)})", 
            sep="\n"
            )
            found = True
    if not found:
        print("Student not found.")


def export_csv():
    if not students:
        print("Student dataset is empty.")
        return
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math", "English", "Science", "Average", "Grade"])
        for s in students:
            average = s.calculate_average()
            writer.writerow([
                s.name, 
                s.math_grade, 
                s.english_grade, 
                s.science_grade, 
                f"{average:.2f}", 
                get_grade(average)]
            )
    print("File exported as students.csv")


def main():
    print("Student Grade Management System")
    load_students()
    print("Data loaded successfully.")
    while True:
        print("\n===== MENU =====",
            "1. Add Student",
            "2. View Students",
            "3. Search Student",
            "4. Edit Student",
            "5. Delete Student",
            "6. Sort Students",
            "7. Statistics",
            "8. Grade Chart",
            "9. Delete All Data",
            "10. View Student Details",
            "11. Export CSV File",
            "12. Exit",
            sep="\n"
        )
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
            sort_students()
        elif choice == "7":
            statistics()
        elif choice == "8":
            grade_chart()
        elif choice == "9":
            delete_all()
        elif choice == "10":
            view_student_details()
        elif choice == "11":
            export_csv()
        elif choice == "12":
            save_students()
            print("Goodbye!")
            break
        else:
            print("Input is not a number from the menu.")
        input("Press Enter to continue.\n")


if __name__ == "__main__":
    main()