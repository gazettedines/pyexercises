"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two answers typed by the user: name (text) and age (typed as text, but it is a number)
# 2. Process: the program keeps both answers. To add 1 to the age, it must be a number, so I use int(). Then, to join the new age with text using +, I change it back into text with str().
# 3. Out: three lines on the screen: "My name is Lam", "My age is 26",and "My name is Lam and my age is 26" (if I type Lam and 25).
# 4. My two fields, and what I would do with them: name and age, from a newsletter sign-up form. I would use the name to greet the customer in emails, and the age to put them in the right age group for offers.


# Your code below
name = input("Enter your name:")
age = int(input("Enter your age:"))

print("My name is ", name )
print("My age is ", age)

print("My name is " + name + " and my age is " + str(age))