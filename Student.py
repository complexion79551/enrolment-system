class Student:
    def __init__(self, name, num):
        self.set_id(num)
        self.set_name(name)
        self.grades = []
        self.courses = []

    def set_id(self, num):
        self.ID = int(num)

    def set_name(self, name):
        self.name = name

    @property
    def get_name(self):
        return self.name

    @property
    def get_id(self):
        return self.ID

    @property
    def get_grades(self):
        return self.grades

    @property
    def get_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def add_grade(self, grade):
        self.grades.append(grade)

    def __str__(self):
        return "Name: %s\t\tID number: %d" % (self.name, self.ID)