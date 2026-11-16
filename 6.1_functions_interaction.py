"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one whole number. In the first part it is written in the code
#    (-4, 5, 9), then typed by the user with int(), then 0 for the last test.
# 2. Process, function by function:
#    - is_zero(num) returns True if the number is 0.
#    - is_positive(num) returns True if the number is above 0.
#    - is_negative(num) returns True if the number is below 0.
#    - is_even(num) returns True if the number can be divided by 2.
#    - detailed_message(num) asks is_zero, then is_positive, then is_negative,
#      and returns a sentence with the first answer that is True.
# 3. Out: one sentence on the screen, for example "The number is zero."
# 4. The question my fourth function answers: "Is this number zero, positive
#    or negative?" Splitting it makes it easier to check, because each small
#    function does one job in one line, so I can test it alone and see at once
#    if it is right. Note: the even/odd part is never reached, because every
#    number is already zero, positive or negative.


# Your code below
number = -4
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

number = 5
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

number = 9
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

def check(number):
    if number > 0:
        print("The number is positive")
    else:
        print("The number is negative")

num = int(input("Enter a number:"))
check(num)



def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

def is_zero(num):
    return num == 0

def is_even(num):
    return num % 2 == 0

def detailed_message(num):
    if is_zero(num):
        return "The number is zero."
    elif is_positive(num):
        return "The number is positive."
    elif is_negative(num):
        return "The number is negative."
    elif is_even(num):
        return "The number is even."
    else:
        return "The number is odd."

number = 0
print(detailed_message(number))