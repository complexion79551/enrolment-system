from Student import *
from Course import *

sList = []
cList = []


def is_id_unique(num):
    for s in sList:
        if s.get_id == num:
            return False
    return True


def is_valid_id(num):
    if num.isdigit() and len(num) == 8:
        return True
    return False


def is_valid_name(string):
    if any(x.isupper() for x in string) and any(x.islower() for x in string):
        return True
    return False


def is_valid_code(string):
    allowed = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-')
    if set(string).issubset(allowed) and len(string) == 7:
        return True
    return False


def compute_gpa(student):
    gpa = 0.0
    total_units = 0.0

    for grade, course in zip(student.get_grades, student.get_courses):
        if grade >= 0:
            gpa += (course.get_unit * grade)
            total_units += course.get_unit

    gpa /= total_units

    return gpa


def display_top_students(course):
    found = False
    new_list = sorted(course.get_students, key=lambda student: student.get_grades[student.get_courses.index(course)], reverse=True)

    for s in new_list[:5]:
        if s.get_grades[s.courses.index(course)] > 0:
            found = True
            print("%s\t\tGrade: %.1f" % (s.get_name, s.get_grades[s.get_courses.index(course)]))

    if not found:
        print("No grades yet for students in %s." % course.get_code)


def display_enrolled_courses(student):
    print("\nList of %s's enrolled courses:" % student.get_name)

    if len(student.get_courses) == 0:
        print("%s is not enrolled in any classes." % student.get_name)
    else:
        for c in student.get_courses:
            print(str(c))


def enter_student(string):
    s_input = str(input("\nEnter ID number of student to %s: " % string))
    student = None

    if is_valid_id(s_input):
        for s in sList:
            if s.get_id == int(s_input):
                student = s

    if student is None:
        print("\nStudent with that ID was not found in the system.")

    return student


def enter_course(string):
    c_input = str(input("\nEnter course to %s: " % string))
    course = None

    if is_valid_code(c_input):
        for c in cList:
            if c.get_code == c_input:
                course = c

    if course is None:
        print("%s was not found in the system." % c_input)

    return course


def course_menu():
    while True:
        print('''                                                          
        ,---.                             ,-.-.               
        |    ,---..   .,---.,---.,---.    | | |,---.,---..   .
        |    |   ||   ||    `---.|---'    | | ||---'|   ||   |
        `---'`---'`---'`    `---'`---'    ` ' '`---'`   '`---'                                           
        ''')
        choice = str(input(
            "Actions:\n1 - Add a course\t2 - Edit a course\t3 - Remove a course\n" +
            "4 - Display courses\t5 - Go back\n\nWhat do you want to do? "))

        if choice == '1':
            while True:
                valid_code = False
                duplicated = False

                if not valid_code:
                    c_name = str(input("\nEnter course code: "))

                if not is_valid_code(c_name):
                    print(
                        "Please enter a valid course code (only uppercase letters, " +
                        "numbers and dashes allowed and be 7 characters).")
                else:
                    for i in cList:
                        if i.get_code == str(c_name):
                            duplicated = True

                    if duplicated:
                        print("\nThat course has already been added.")
                    else:
                        valid_code = True
                        break

            while True:
                valid_unit = False

                if not valid_unit:
                    c_unit = str(input("Enter number of units: "))

                if c_unit.replace('.', '', 1).isdigit():
                    if 1 <= float(c_unit) <= 4 and float(c_unit) % 1.0 == 0:
                        valid_unit = True
                        break
                    else:
                        print("Please enter a valid course unit.\n")
                else:
                    print("Invalid input!\n")

            if valid_code and valid_unit:
                cList.append(Course(c_name, c_unit))
                print("\nCourse added successfully.")

        elif choice == '2':
            if len(cList) == 0:
                print("There are no courses in the system.")
            else:
                course = enter_course("edit")
                if course is not None:
                    while True:
                        choice = str(input("Actions:\n1 - Edit course code\t2 - Edit number of units" +
                                           "\n\nWhat do you want to do? "))

                        if choice == '1':
                            while True:
                                duplicated = False

                                c_name = str(input("\nEnter new course code: "))

                                if not is_valid_code(c_name):
                                    print(
                                        "Please enter a valid course code (only uppercase letters, " +
                                        "numbers and dashes allowed and be 7 characters).")
                                else:
                                    for c in cList:
                                        if c.get_code == str(c_name):
                                            duplicated = True

                                    if duplicated:
                                        print("\nThe new course code cannot be the same " +
                                              "as another course in the system.")
                                    else:
                                        course.set_code(c_name)
                                        print("\nCourse code was successfully updated.")
                                        break
                            break

                        elif choice == '2':
                            while True:
                                c_input = str(input("\nEnter new number of units: "))

                                if c_unit.replace('.', '', 1).isdigit():
                                    if float(c_unit) >= 1 and float(c_unit) <= 4 and float(c_unit) % 1.0 == 0:
                                        course.set_unit(c_input)
                                        print("\nNumber of units was successfully updated.")
                                        break
                                    else:
                                        print("Please enter a value from 0 to 4.\n")
                                else:
                                    print("Invalid input!\n")
                            break

                        else:
                            print("Invalid input!\n")

        elif choice == '3':
            if len(cList) == 0:
                print("There are no courses in the system.")
            else:
                course = enter_course("remove")
                if course is not None:
                    cList.remove(course)

                    if len(sList) > 0:
                        for s in sList:
                            if len(s.get_courses) > 0:
                                for c in s.get_courses:
                                    if c.get_code == course.get_code:
                                        s.get_grades[s.get_courses.index(c)] = -1
                                        s.remove_course(c)
                    print("\n%s was successfully removed from the system." % course.get_code)

        elif choice == '4':
            if len(cList) == 0:
                print("No classes to display.")
            else:
                for c in cList:
                    print("==============================================\n" + str(c))
                    print("\nList of students enrolled in %s:" % c.get_code)

                    if len(c.get_students) == 0:
                        print("No students are enrolled in %s." % c.get_code)
                    else:
                        for s in c.get_students:
                            print(str(s))

                        print("\nThe top students of the class are:")
                        display_top_students(c)

        elif choice == '5':
            main_menu()
            break

        else:
            print("Invalid input!\n")


def student_menu():
    while True:
        print('''                                                   
        ,---.|             |          |        ,-.-.               
        `---.|--- .   .,---|,---.,---.|---     | | |,---.,---..   .
            ||    |   ||   ||---'|   ||        | | ||---'|   ||   |
        `---'`---'`---'`---'`---'`   '`---'    ` ' '`---'`   '`---'                                                    
        ''')
        choice = str(input("Actions:\n1 - Add a student\t2 - Edit student info\t3 - Remove a student\n" +
                           "4 - Enroll a student\t5 - Drop a student\t6 - Input student's grade\n" +
                           "7 - View student's grades\t\t\t8 - View list of students\n" +
                           "9 - Go back\n\nWhat do you want to do? "))

        if choice == '1':
            while True:
                valid_name = False
                if not valid_name:
                    s_name = str(input("\nEnter student name (<First name> <Surname>): "))

                if not is_valid_name(s_name):
                    print("Please enter a valid name.")
                else:
                    valid_name = True
                    break

            while True:
                valid_id = False
                if not valid_id:
                    s_id = str(input("Enter student ID: "))

                if not is_valid_id(s_id):
                    print("Please enter a valid ID number.\n")
                elif not is_id_unique(int(s_id)):
                    print("Please enter a unique ID number.\n")
                else:
                    valid_id = True
                    break

            if valid_name and valid_id:
                sList.append(Student(s_name, s_id))
                print("\nStudent was successfully added to the system.")

        elif choice == '2':
            if len(sList) == 0:
                print("There are no students in the system.")
            else:
                student = enter_student("edit")
                if student is not None:
                    while True:
                        choice = str(input("Actions:\n1 - Edit name\t2 - Edit ID number\n\nWhat do you want to do? "))

                        if choice == '1':
                            while True:
                                s_input = str(input("\nEnter %s's new name: " % student.get_name))

                                if not is_valid_name(s_input):
                                    print("Please enter a valid name.")
                                else:
                                    student.set_name(s_input)
                                    print("\nName was successfully updated.")
                                    break
                            break

                        elif choice == '2':
                            while True:
                                s_input = str(input("\nEnter %s's new student ID: " % student.get_name))

                                if not is_valid_id(s_input):
                                    print("Please enter a valid ID number.\n")
                                elif not is_id_unique(int(s_input)):
                                    print("Please enter a unique ID number.\n")
                                else:
                                    student.set_id(s_input)
                                    print("\nID number was successfully updated.")
                                    break
                            break

                        else:
                            print("Invalid input!\n")

        elif choice == '3':
            if len(sList) == 0:
                print("There are no students in the system.")
            else:
                student = enter_student("remove")
                if student is not None:
                    sList.remove(student)
                    if len(cList) > 0:
                        for c in cList:
                            if len(c.get_students) > 0:
                                for s in c.get_students:
                                    if s.get_name == student.get_name:
                                        c.remove_student(s)
                    print("\n%s was successfully removed from the system." % student.get_name)

        elif choice == '4':
            if len(sList) == 0:
                print("There are no students in the system.")
            else:
                student = enter_student("enroll")
                if student is not None:
                    course = enter_course("enroll %s in" % student.get_name)

                    if course is not None:
                        enroll = None
                        for c in student.get_courses:
                            if c == course:
                                enroll = c

                        if enroll is not None:
                            print("\n%s is already enrolled in %s." % (student.get_name, course.get_code))
                        else:
                            student.add_course(course)
                            student.add_grade(-1)
                            course.add_student(student)
                            print("\n%s was successfully added to the %s class list."
                                  % (student.get_name, course.get_code))

        elif choice == '5':
            if len(sList) == 0:
                print("There are no students in the system.")
            else:
                student = enter_student("drop")
                if student is not None:
                    if len(student.get_courses) == 0:
                        print("%s is not enrolled in any classes." % student.get_name)
                    else:
                        display_enrolled_courses(student)
                        c_input = str(input("\nEnter course to drop %s from: " % student.get_name))

                        in_class_list = False

                        if is_valid_code(c_input):
                            for c in cList:
                                if c.get_code == c_input:
                                    in_class_list = True

                        if in_class_list:
                            course = None

                            for c in student.get_courses:
                                if c.get_code == c_input:
                                    course = c

                            if course is None:
                                print("\n%s is not enrolled in %s." % (student.get_name, c_input))
                            else:
                                student.get_grades[student.get_courses.index(course)] = -1
                                student.remove_course(course)
                                course.remove_student(student)
                                print("\n%s was successfully removed from the %s class list." % (
                                    student.get_name, course.get_code))

                        else:
                            print("\n%s was not found in the system." % c_input)

        elif choice == '6':
            if len(sList) == 0:
                print("There are no students in the system.")
            else:
                student = enter_student("add their grade")
                if student is not None:
                    if len(student.get_courses) == 0:
                        print("%s is not enrolled in any course." % student.get_name)
                    else:
                        display_enrolled_courses(student)
                        c_input = str(input("\nEnter course to add %s's grade to: " % student.get_name))

                        enrolled = False
                        in_class_list = False

                        if is_valid_code(c_input):
                            for c in cList:
                                if c.get_code == c_input:
                                    in_class_list = True

                        if in_class_list:
                            for c in student.get_courses:
                                if c.get_code == c_input:
                                    enrolled = True
                                    course = c
                                    if student.get_grades[student.get_courses.index(course)] > 0:
                                        added = True

                            if not enrolled:
                                print("\n%s is not enrolled in %s." % (student.get_name, c_input))
                            else:
                                while True:
                                    grade = str(input("\nEnter %s's grade in %s: " % (student.get_name, course.get_code)))

                                    if grade.replace('.', '', 1).isdigit():
                                        if 0 <= float(grade) <= 4.0 and float(grade) % 0.5 == 0:
                                            student.get_grades[student.get_courses.index(course)] = float(grade)
                                            print("\n%s's grade in %s was successfully set." % (
                                                student.get_name, course.get_code))
                                            break
                                        else:
                                            print("Please enter a valid final grade.")
                                    else:
                                        print("Invalid input!\n")
                        else:
                            print("\n%s was not found in the system." % c_input)

        elif choice == '7':
            if len(sList) == 0:
                print("There are no students in the system.")
            else:
                student = enter_student("view their grades")
                empty = False

                if student is not None:
                    if len(student.get_courses) == 0:
                        print("%s is not enrolled in any classes." % student.get_name)
                    else:
                        print("=====================================================\n" +
                              "Grade report for %s: " % student.get_name)
                        for grade, course in zip(student.get_grades, student.get_courses):
                            if grade >= 0.0:
                                print(
                                    "Course: %s\tGrade: %.1f\tUnits: %.1f" % (course.get_code, grade, course.get_unit))
                            else:
                                empty = True

                        if empty:
                            print("No grades to display.")
                        else:
                            print("GPA: %.3f" % compute_gpa(student))

        elif choice == '8':
            if len(sList) == 0:
                print("No students to display.")
            else:
                for s in sList:
                    print("================================================\n" + str(s))
                    display_enrolled_courses(s)

        elif choice == '9':
            main_menu()
            break

        else:
            print("Invalid input!\n")


def main_menu():
    print('''
  ______                 _ _                      _      _____           _                 
 |  ____|               | | |                    | |    / ____|         | |                
 | |__   _ __  _ __ ___ | | |_ __ ___   ___ _ __ | |_  | (___  _   _ ___| |_ ___ _ __ ___  
 |  __| | '_ \| '__/ _ \| | | '_ ` _ \ / _ \ '_ \| __|  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |____| | | | | | (_) | | | | | | | |  __/ | | | |_   ____) | |_| \__ \ ||  __/ | | | | |
 |______|_| |_|_|  \___/|_|_|_| |_| |_|\___|_| |_|\__| |_____/ \__, |___/\__\___|_| |_| |_|
                                                                __/ |                      
                                                               |___/                       
    ''')
    while True:
        choice = str(input("\t\t1 - Course Menu\t\t\t2 - Student Menu\nWhere do you want to go? "))

        if choice == '1':
            course_menu()
            break
        elif choice == '2':
            student_menu()
            break
        else:
            print("Invalid input!\n")


main_menu()