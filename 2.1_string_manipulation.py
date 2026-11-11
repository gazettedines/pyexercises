"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one line typed by the user: a full name, last name first, like in Vietnamese, 
#    for example "Nguyen Thi Thanh Lam" (text)
# 2. Process: the program removes the spaces at both ends, cuts the name into words 
#    with split(), takes the first word as the last name and and the rest as the first 
#    name, then changes them in four differet ways with lower(), replace(), title(), 
#    upper() and join().
# 3. Out: four lines on the screen: a school email, the full name in French style, 
#    a CV file name, and a short name for a badge
# 4. My four transformations, and when each is useful: 
#    - Email: create the SKEMA email of a new student from their name.
#    - Full name: write the name the French way, last name in capitals, for offical papers
#    - CV file: name a CV file without space, so it looks clean when I apply for a job
#    - Badge: print the short name people call me, for an event or a student card


# Your code below
# Ask for the full name, last name first, like in Vietnamese
full = input("Type your full name (last name first): ")

# Cut the name into words: the first word is the last name, the rest is the first name
words = full.strip().split()
last = words[0]
first = " ".join(words[1:])

# 1. School email: first name in small letters without spaces, a dot, then the last name
print("Email     :", first.lower().replace(" ", "") + "." + last.lower() + "@skema.edu")

# 2. French style: first name with capitals, then the last name in CAPITALS
print("Full name :", first.title() + " " + last.upper())

# 3. CV file name: spaces replaced by "_"
print("CV file   :", "_".join(words).title() + ".pdf")

# 4. Badge: the name people call me (the last word) and the last name in CAPITALS
print("Badge     :", words[-1].title() + " " + last.upper())