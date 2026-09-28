class Student:

    def __init__(self, name, math_grade, english_grade, science_grade):
        self.name = name
        self.math_grade = math_grade
        self.english_grade = english_grade
        self.science_grade = science_grade

    def calculate_average(self):
        average = (
            self.math_grade +
            self.english_grade +
            self.science_grade
        ) / 3

        return average