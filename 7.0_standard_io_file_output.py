"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: four answers typed by the user about one student: first name,
#    last name, date of birth and student number (all kept as text).
# 2. Process: the program checks if the CSV file already exists. It opens the
#    file in "a" mode, which adds at the end instead of erasing. It writes the
#    header line only the first time, then one line with the four answers
#    separated by commas.
# 3. Out, file name and columns: 7.0_student_data.csv, with the columns
#    First Name, Last Name, Date of Birth, Student Number. One new line per run.
# 4. Why these columns, and what this file is for: a list of the students in a
#    class. With 200 rows, I could find a student by their number, count the
#    students, or send a birthday message using the date of birth.
#
# First run: the file does not exist, so the program writes the header first.
# Bad value: the program does not check what the user types. An empty name
# or a wrong date is saved as it is. I accept this for now / I would refuse
# empty values by ... (quyết định của bạn)


# Your code below
import os

# Ask the user for one student's details
print("Please fill in the following details:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth = input("Date of Birth (DD/MM/YYYY): ")
student_number = input("Student Number: ")

# Check if the file already exists BEFORE opening it
file_exists = os.path.exists("7.0_student_data.csv")

# "a" adds at the end of the file, so each run adds one line and nothing is erased
with open("7.0_student_data.csv", "a", newline="") as file:
    # Write the header only the very first time, when the file does not exist yet
    if not file_exists:
        file.write("First Name,Last Name,Date of Birth,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth + "," + student_number + "\n")

print("Data saved successfully!")