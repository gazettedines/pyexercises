"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number N typed by the user. input() gives text, so int() turns it into 
#    a whole number
# 2. Process: the program first checks the number. If it is 0, negative or bigger than 
#    100, it shows a message and stops there. Otherwise, it goes through every number 
#    from 1 to N and uses % 2 (the remainder after dividing by 2) to decide if each one 
#    is odd or even
# 3. Out: on the screen, one line per number, for example "1 is odd", "2 is even"... up 
#    to N. Or one message if the number is not accepted
# 4. What happens on 0, on a negative number, on a very large number: 
#    - 0: a message, because there is no number between 1 and 0 to check. 
#    - negative: refused with a message, because counting from 1 up to a negative number 
#      makes no sense
#    - 5000: refused above 100, because 5000 lines would be too long to read on the 
#      screen and nobody would read them


# Your code below
# Ask for a number and turn it into a whole number
N = int(input("Enter a number: "))

# 0: there is no number between 1 and 0, so there is nothing to check 
if N == 0:
    print("Nothing to check: please type a number bigger than 0.")

# Negative number: counting from 1 up to a negative number makes no sense
elif N < 0:
    print("Negative numbers are not accepted.")

# Too big: more than 100 lines would be too long to read on the screen
elif N > 100:
    print("Too many numbers: please type 100 or less.")

# Normal case: Go through every number from 1 to n (n+1 because range stops just before it)
for i in range(1, N + 1):
    # If the number can be divided by 2 with nothing left, it is even
    if i % 2 == 0:
        print(i, "is even")
    # Otherwise there is 1 left, so it is odd
    else:
        print(i, "is odd")
