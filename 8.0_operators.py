"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers typed by the user, turned into numbers with float(),
#    so they are compared as numbers, not as text.
# 2. Process: the program compares them with the six comparison operators
#    (==, !=, <, >, <=, >=), then combines some results with and, or, not.
# 3. Out: a small table on the screen, one comparison per line with True/False.
# 4. My two values, and the surprise: I typed 1000 and 1e3. The surprise is
#    that a == b is True: Python reads 1e3 as 1 x 10^3, which is 1000.


# Your code below

# My two values, typed by the user and turned into numbers
a = float(input("First number: "))
b = float(input("Second number: "))

# Every comparison between them, with a label to show in the table
results = [
    ("a == b", a == b),
    ("a != b", a != b),
    ("a < b", a < b),
    ("a > b", a > b),
    ("a <= b", a <= b),
    ("a >= b", a >= b),
]

# Show the table: ljust(12) adds spaces so the results line up in a column
print("Comparison".ljust(12), "Result")
print("-" * 20)
for label, value in results:
    print(label.ljust(12), value)

# Logical combinations of the results: and, or, not
print()
print("(a == b) and (a < b)".ljust(26), (a == b) and (a < b))
print("(a == b) or (a < b)".ljust(26), (a == b) or (a < b))
print("not (a == b)".ljust(26), not (a == b))
