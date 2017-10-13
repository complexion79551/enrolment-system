class Course:
    def __init__(self, code, unit):
        self.set_code(code)
        self.set_unit(unit)
        self.students = []

    def set_code(self, code):
        self.code = code

    def set_unit(self, unit):
        self.unit = float(unit)

    @property
    def get_code(self):
        return self.code

    @property
    def get_unit(self):
        return self.unit

    @property
    def get_students(self):
        return self.students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def __str__(self):
        return "Course: %s\t\t\tUnits: %s" % (self.code, self.unit)