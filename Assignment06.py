# --------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error
#          handling.
# Change Log: (Who, When, What)
#   N.Greco, 11/15/2024, Created Script
#   N.Greco, 11/16/2024, Updated Output Formatting in Functions
# --------------------------------------------------------------------------- #
import json

# Define the data constants.
FILE_NAME: str = "Enrollments.json" # Removed old Enrollments.csv reference.
MENU: str = """
----- Course Registration Program -----
  Select from the following menu:
   1. Register a Student for a Course
   2. Show Current Data
   3. Save Data to a File
   4. Exit the Program
---------------------------------------
"""

# Define the data variables.
menu_choice: str        # Hold the choice made by the user.
students: list = []     # Holds a table of student data.

# Removed all of these variables and used them locally instead:
    # course_name: str = ''  # Holds the name of a course entered by the user.
    # csv_data: str = ''  # Holds combined string data separated by a comma.
    # file = None  # Holds a reference to an opened file.
    # json_data: str = ''  # Holds combined string data in a json format.
    # student_data: dict = {}  # Holds one row of student data.
    # student_first_name: str = ''  # Holds the first name of a student
    #                                 entered by the user.
    # student_last_name: str = ''  # Holds the last name of a student entered
    #                                by the user.

# Processing ---------------------------------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    ChangeLog: (Who, When, What)
    N.Greco, 11/15/2024, Created Class
    """


    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        A function that extracts data from a JSON file.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function
        N.Greco, 11/16/2024, Updated Output Formatting

        :return: A list with student data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("\n!!! JSON file must exist " \
                    "before running this script. !!!", e)
        except Exception as e:
            IO.output_error_messages("\nThere was a non-specific error!", e)
        finally:
            if not file.close():
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        A function that writes data to a JSON file.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function
        N.Greco, 11/16/2024, Updated Output Formatting

        :return: A list with student data
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data)
        except TypeError as e:
            IO.output_error_messages("\nPlease check that data is valid JSON \
                formatting!", e)
        except Exception as e:
            IO.output_error_messages("\nThere was a non-specific error!", e)
        finally:
            if not file.close():
                file.close()


# Presentation -------------------------------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and
    output.

    ChangeLog: (Who, When, What)
    N.Greco, 11/15/2024, Created Class
    """


    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        A function that displays a custom error message to the user.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function

        :return: None
        """
        print(message, end = "\n")
        if error is not None:
            print("\n----------- Technical Error Message -----------")
            print(error, error.__doc__, type(error), sep = "\n")


    @staticmethod
    def output_menu(menu: str):
        """
        A function that displays the menu of choices to the user.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function

        :return: None
        """
        print(menu)


    @staticmethod
    def input_menu_choice():
        """
        A function that requests the menu choice from the user.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function
        N.Greco, 11/16/2024, Updated Output Formatting

        :return: None
        """
        choice = "0"
        try:
            choice = input("What would you like to do? ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("\n!!! Please choose a menu option " \
                                    "(1, 2, 3, or 4). !!!")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice


    @staticmethod
    def output_student_courses(student_data: list):
        """
        A function that displays current student data.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function
        N.Greco, 11/16/2024, Updated Output Formatting

        :return: None
        """
        # Process the data to create and display a custom message
        print("\n" + "-" * 60)
        for student in student_data:
            print(f"\t{student["FirstName"]} {student["LastName"]} "\
                  f"is enrolled in {student["CourseName"]}")
        print("-" * 60)


    @staticmethod
    def input_student_data(student_data: list):
        """
        A function that requests student data from the user.

        ChangeLog: (Who, When, What)
        N.Greco, 11/15/2024, Created Function
        N.Greco, 11/16/2024, Updated Output Formatting

        :return: None
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain letters!")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain letters!")

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"\nYou have registered {student_first_name} {student_last_name}" \
                    f" for {course_name}.")
        except ValueError as e:
            IO.output_error_messages('\nThat value is not the correct type of data!', e)
        except Exception as e:
            IO.output_error_messages("\nThere was a non-specific error!", e)
        return students


# Main body of script. Starts by reading in JSON file data.
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

# Repeat the following tasks.
while True:

    # Present the menu of choices and request user selection.
    IO.output_menu(menu = MENU)
    menu_choice = IO.input_menu_choice()

    # Input user student data.
    if menu_choice == "1":
        students = IO.input_student_data(student_data = students)
        continue

    # Present the current student data.
    elif menu_choice == "2":
        IO.output_student_courses(student_data = students)
        continue

    # Save the data to a JSON file.
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    # Stop the loop and exit the program.
    elif menu_choice == "4":
        print("\n" + "-" * 35)
        print("*** Exiting Program. Thank you! ***")
        print("-" * 35)
        break  # out of the loop