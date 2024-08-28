# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   David Levinson,8/24/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data in dict form
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file, with added exception handling
try:
    file = open(FILE_NAME, 'r')
    # Transform the data from the file
    for row in file.readlines():
        parts = row.strip().split(",")
        student_first_name = parts[0]
        student_last_name = parts[1]
        course = parts[2]
        student_data = {'First_Name': student_first_name, 'Last_Name': student_last_name, 'Course': course}
        students.append(student_data)
except FileNotFoundError as errortext:
    print("Text file must exist before running this script!\n")
except Exception as errortext:
    print("There was a non-specific error!\n")
    print("Built-In Python error info: ")
    print(errortext, errortext.__doc__, type(errortext), sep='\n')
finally:
    if file:
        file.close()
# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        while True:
            try:
                student_first_name: str = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("First name must contain only alphabetic characters.")
                break
            except ValueError as errortext:
                print(errortext)
        while True:
            try:
                student_last_name: str = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("Last name must contain only alphabetic characters.")
                break
            except ValueError as errortext:
                print(errortext)

        course: str = input("Please enter the name of the course: ")
        student_data: dict = {'First_Name': student_first_name,
                              'Last_Name': student_last_name,
                              'Course': course}
        students.append(student_data)
        continue

    # Present the current data
    if menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for row in students:
            print(f"{row['First_Name']} {row['Last_Name']} is registered for {row['Course']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for row in students:
                csv_data = f'{row["First_Name"]},{row["Last_Name"]},{row["Course"]}\n'
                file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for row in students:
                print(f"{row['First_Name']} {row['Last_Name']} is registered for {row['Course']}")
        except  TypeError as errortext:
            print(errortext)
        except Exception as errortext:
            print(errortext)
        finally:
            if file:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
