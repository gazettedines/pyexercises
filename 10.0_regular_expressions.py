"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three values typed by the user about a SKEMA student: school email,
#    student number, date of birth.
# 2. Process: each value is checked against a pattern with re.fullmatch().
#    Each field is tested on its own, so I can say which one is wrong.
#    The values are saved to a CSV file only if all three pass.
# 3. Out: "Saved" and one new line in students_checked.csv, or the list of
#    fields that were refused, and nothing saved.
# 4. My three fields and their rules: see the comment above each rule below.

import re
import os

FILE_NAME = "students_checked.csv"

# Email rule: small letters, one dot, small letters, then exactly @skema.edu.
# [a-z]+ = one or more small letters; \. = a real dot (a plain . means "any
# character"); @skema\.edu = exactly that text.
EMAIL_RULE = r"[a-z]+\.[a-z]+@skema\.edu"

# Student number rule: exactly 6 digits, nothing else.
# \d = one digit; {6} = exactly 6 times.
NUMBER_RULE = r"\d{6}"

# Date rule: two digits / two digits / four digits, like 29/01/2002.
# It checks the SHAPE only: 99/99/2002 still passes.
DATE_RULE = r"\d{2}/\d{2}/\d{4}"


# Ask for the three values (lower() so that capitals in the email are accepted)
email = input("SKEMA email: ").strip().lower()
number = input("Student number (6 digits): ").strip()
birth = input("Date of birth (DD/MM/YYYY): ").strip()

# Check each field separately, and keep the names of the ones that fail
refused = []
if re.fullmatch(EMAIL_RULE, email) is None:
    refused.append("email")
if re.fullmatch(NUMBER_RULE, number) is None:
    refused.append("student number")
if re.fullmatch(DATE_RULE, birth) is None:
    refused.append("date of birth")

# Save only when all three are acceptable
if len(refused) == 0:
    file_exists = os.path.exists(FILE_NAME)
    with open(FILE_NAME, "a", newline="") as file:
        if not file_exists:
            file.write("Email,Student Number,Date of Birth\n")
        file.write(email + "," + number + "," + birth + "\n")
    print("Saved.")
else:
    print("Not saved. Please check:", ", ".join(refused))
