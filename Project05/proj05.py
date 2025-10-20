#######################################################################################################################
#
# Computer Project 05
#
#######################################################################################################################

import csv
from operator import itemgetter


def open_file(prompt):
    while True:
        try:
            filename = input(prompt)
            file = open(filename, 'r')
            return file
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")


def read_csv_file(file):
    names = []
    for line in file:
        names.append(line.strip())  # Stripping any whitespace or newlines
    file.close()
    return names


def read_txt_file(file):
    grades = []
    for line in file:
        # Split by comma, convert to integer, and handle missing data
        grades.append([int(x) if x else 0 for x in line.strip().split(',')])
    file.close()
    return grades


def read_all_files():
    # Open all necessary files
    names_file = open_file("Enter the student names file (e.g., Names.csv): ")
    english_file = open_file("Enter the English grades file (e.g., english_id.txt): ")
    math_file = open_file("Enter the Math grades file (e.g., math_id.txt): ")
    science_file = open_file("Enter the Science grades file (e.g., science_id.txt): ")

    names = read_csv_file(names_file)
    english_grades = read_txt_file(english_file)
    math_grades = read_txt_file(math_file)
    science_grades = read_txt_file(science_file)

    master_list = []
    for i in range(len(names)):
        student_data = {
            'name': names[i],
            'English': english_grades[i] if i < len(english_grades) else [0, 0, 0, 0],
            'Math': math_grades[i] if i < len(math_grades) else [0, 0, 0],
            'Science': science_grades[i] if i < len(science_grades) else [0, 0, 0]
        }
        master_list.append(student_data)

    return master_list


def find_max_grade(master_list, student_name):
    for student in master_list:
        if student['name'].lower() == student_name.lower():
            english_total = sum(student['English'])
            math_total = sum(student['Math'])
            science_total = sum(student['Science'])

            max_grade = max(english_total, math_total, science_total)
            subject = 'English' if max_grade == english_total else 'Math' if max_grade == math_total else 'Science'

            return max_grade, subject
    return None, None


def calculate_average_grade(master_list, student_name):
    for student in master_list:
        if student['name'].lower() == student_name.lower():
            english_total = sum(student['English'])
            math_total = sum(student['Math'])
            science_total = sum(student['Science'])
            average_grade = (english_total + math_total + science_total) / 3
            return round(average_grade, 1)
    return None


def main():
    master_list = read_all_files()

    menu = '''
    Menu:
     1: The maximum grade a student received in a single subject
     2: The average subject grade a student received
     3: Individual information
     4: The average grade of a subject over all students
     5: The number of students with an average grade exceeding given threshold X
     6: The name of student having the highest average grade
     7: The name of student having the highest grade of given subject name
     Enter any other key(s) to exit
    '''

    while True:
        print(menu)
        choice = input("Enter a choice: ")

        if choice == '1':
            student_name = input("Enter a student name: ")
            max_grade, subject = find_max_grade(master_list, student_name)
            if max_grade:
                print(f"The highest grade for {student_name} is {max_grade} in {subject}.")
            else:
                print("Student not found.")

        elif choice == '2':
            student_name = input("Enter a student name: ")
            average_grade = calculate_average_grade(master_list, student_name)
            if average_grade is not None:
                print(f"The average grade for {student_name} is {average_grade}.")
            else:
                print("Student not found.")


        else:
            print("Thank you")
            break


if __name__ == '__main__':
    main()

# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()