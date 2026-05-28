
from auth import register_menu
from services.course_service import course_menu
from services.grade_service import grade_menu
from services.student_service import enrollment_menu, student_menu
from services.teacher_service import teacher_menu

# TODO: Admin Dashboard


def admin_menu(user):

    while True:

        print("""
===== ADMIN MENU =====

1. Students
2. Teachers
3. Courses
4. Enrollment
5. Grades
6. Register User
7. Logout
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            student_menu()

        elif choice == "2":
            teacher_menu()

        elif choice == "3":
            course_menu()

        elif choice == "4":
            enrollment_menu()

        elif choice == "5":
            grade_menu()

        elif choice == "6":
            register_menu(user)

        elif choice == "7":
            print("Logging out...")
            back_to_login = input("Go back to login? (y/n): ").strip().lower()
            if back_to_login == "y":
                print("Exiting...")
                break
            else:
                continue

# TODO: Teacher Dashboard


def teacher_dashboard(user):

    while True:

        print("""
===== TEACHER MENU =====

1. View Students
2. View Courses
3. Add Grades
4. Logout
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            student_menu()

        elif choice == "2":
            course_menu()

        elif choice == "3":
            grade_menu()

        elif choice == "4":
            print("Logging out...")
            back_to_login = input("Go back to login? (y/n): ").strip().lower()
            if back_to_login == "y":
                print("Exiting...")
                break
            else:
                continue

# TODO: Student Dashboard


def student_dashboard(user):

    while True:

        print("""
===== STUDENT MENU =====

1. View Courses
2. View Grades
3. Logout
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            course_menu()

        elif choice == "2":
            grade_menu()

        elif choice == "3":
            print("Logging out...")
            back_to_login = input("Go back to login? (y/n): ").strip().lower()
            if back_to_login == "y":
                print("Exiting...")
                break
            else:
                continue
