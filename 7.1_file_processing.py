"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Empty lines: one after "grace hopper" and one after "GUIDO van rossum".
# - Spaces at the start of some lines: "  alan TURING", "  linus torvalds".
# - Capitals are mixed: some last names are all in capitals (LOVELACE, TURING),
#   some names are all small (grace hopper), "GUIDO" is all capitals.
# - One name has three words: "GUIDO van rossum". "van" is part of the last
#   name, so the last name is "van Rossum", and "van" stays in small letters.

# 1. In: names.txt, one person per line, written in a messy way.
# 2. Process, problem by problem:
#    - Empty lines: skipped, they are not names.
#    - Extra spaces: removed with strip(), at both ends.
#    - Mixed capitals: every word is put in small letters, then gets a capital
#      at the start, except small linking words like "van".
#    - Three-word name: I keep all the words, and sort on the last one.
#    Then the names are sorted by last name and written to a new file.
# 3. Out: names_clean.txt, one clean name per line ("Ada Lovelace"), sorted by
#    last name. names.txt is only read, never changed.
# 4. How I decide which word is the last name: the last word of the line. For
#    "Guido van Rossum", the full last name is "van Rossum", but I sort on
#    "Rossum", because the main part of the name is Rossum and "van" is only a
#    linking word.


# Your code below

# Small linking words that are part of a last name and stay in small letters
SMALL_WORDS = ["van", "von", "de", "da", "le"]

# Clean one line: remove spaces, fix the capitals, keep "van" in small letters
def clean_name(line):
    words = line.strip().lower().split()
    cleaned = []
    for word in words:
        if word in SMALL_WORDS:
            cleaned.append(word)
        else:
            cleaned.append(word.capitalize())
    return " ".join(cleaned)

# The word used to sort a name: its last word
def last_name_key(name):
    return name.split()[-1]


# Read every line of the original file (read only, it is never changed)
with open("names.txt", encoding="utf-8") as source:
    lines = source.readlines()

# Keep only the lines that contain a name, and clean each one
names = []
for line in lines:
    if line.strip() == "":
        continue
    names.append(clean_name(line))

# Sort the clean names by last name
sorted_names = sorted(names, key=last_name_key)

# Write the result to a NEW file, one name per line
with open("names_clean.txt", "w", encoding="utf-8") as output:
    for name in sorted_names:
        output.write(name + "\n")

# Show the two counts for the check
print("Lines in names.txt      :", len(lines))
print("Names in names_clean.txt:", len(sorted_names))