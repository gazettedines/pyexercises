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

# 1. In: four answers typed by the user about one student: first name, last
#    name, date of birth (DD/MM/YYYY) and student number.
# 2. Process: each answer is checked by a small function before it is kept:
#    - is_valid_name: the name is not empty and has no comma (a comma would
#      add a column and break the CSV),
#    - is_valid_date: the date has the shape DD/MM/YYYY, with digits only,
#    - is_valid_number: the student number has digits only.
#    If an answer fails, ask() shows "Not accepted" and asks again.
#    Then the program checks if the file already exists, opens it in "a" mode
#    (add at the end, never erase), writes the header only the first time,
#    and adds one line with the four answers separated by commas.
# 3. Out, file name and columns: 7.0_student_data.csv, with the columns
#    First Name, Last Name, Date of Birth, Student Number. Each run adds one
#    line, and the header appears only once.
# 4. Why these columns, and what this file is for: a register of the students
#    in a class. The student number identifies each student, even when two
#    have the same name. The date of birth lets me count ages or send a
#    birthday message. With 200 rows, I could find a student by number, check
#    for duplicates, or sort the class by last name.


# Your code below
import os

FILE_NAME = "7.0_student_data.csv"

# A name is accepted if it is not empty and has no comma (a comma would break the CSV)
def is_valid_name(text):
    return text != "" and "," not in text

# A date is accepted if it looks like DD/MM/YYYY: three parts, all digits, 2-2-4 long
def is_valid_date(text):
    parts = text.split("/")
    return (len(parts) == 3 and len(parts[0]) == 2 and len(parts[1]) == 2
            and len(parts[2]) == 4 and parts[0].isdigit() and parts[1].isdigit()
            and parts[2].isdigit())

# A student number is accepted if it contains only digits
def is_valid_number(text):
    return text.isdigit()

# Ask a question again and again until the answer passes its check
def ask(question, is_valid):
    answer = input(question).strip()
    while not is_valid(answer):
        print("Not accepted, please try again.")
        answer = input(question).strip()
    return answer


# Ask for one student's details, each one checked
print("Please fill in the following details:")
first_name = ask("First Name: ", is_valid_name)
last_name = ask("Last Name: ", is_valid_name)
birth = ask("Date of Birth (DD/MM/YYYY): ", is_valid_date)
student_number = ask("Student Number: ", is_valid_number)

# Check if the file exists BEFORE opening it, to know if the header is needed
file_exists = os.path.exists(FILE_NAME)

# "a" adds one line at the end; the header is written only the first time
with open(FILE_NAME, "a", newline="") as file:
    if not file_exists:
        file.write("First Name,Last Name,Date of Birth,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth + "," + student_number + "\n")

print("Data saved successfully!")