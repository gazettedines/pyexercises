"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: four permission names typed by the user: two to combine, one to
#    test and add, one to remove (view, edit, publish or budget).
# 2. Process: each name is cleaned with strip() and lower(), then checked in a
#    dictionary that gives its bit. The two first ones are combined with |,
#    the third is tested with & and added with |, the fourth is removed with & ~.
# 3. Out: at each step, the permissions in binary (4 bits) and as a number,
#    and True/False for the test.
# 4. What my permissions are about: who can do what on an ads campaign in a
#    marketing team: view it, edit it, publish it, change its budget.


# Your code below

# My four permissions on an ads campaign: each name gives its own bit
PERMISSIONS = {"view": 1, "edit": 2, "publish": 4, "budget": 8}

# Show a step: its name, the value in binary on 4 bits, and as a number
def show(step, value):
    print(step.ljust(28), format(value, "04b"), "=", value)

# Ask for a permission name until it is one of the four I know
def ask_permission(question):
    name = input(question).strip().lower()
    while name not in PERMISSIONS:
        print("Unknown permission. Choose: view, edit, publish, budget")
        name = input(question).strip().lower()
    return name


# Combine two permissions chosen by the user
first = ask_permission("First permission to give: ")
second = ask_permission("Second permission to give: ")
user = PERMISSIONS[first] | PERMISSIONS[second]
show("Combined: " + first + " + " + second, user)

# Test a third permission, then add it
test = ask_permission("Permission to test: ")
print("Does the user have", test + "?", (user & PERMISSIONS[test]) != 0)
user = user | PERMISSIONS[test]
show("After adding " + test, user)

# Remove one permission
remove = ask_permission("Permission to remove: ")
user = user & ~PERMISSIONS[remove]
show("After removing " + remove, user)

# Check: reading the bits myself, from right to left (view, edit, publish, budget):
# ... -> ...