"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the function add_numbers receives two numbers, num1 and num2. In the
#    last part, the two numbers are typed by the user and changed with float().
# 2. Process: the function adds the two numbers.
# 3. Out: the function prints the sum AND returns it. So when I write
#    sum = add_numbers(10, 20) and then print(sum), the sum appears twice.
# 4. My function name, and why return rather than print: add_numbers. The name
#    says what it does without reading the code. return matters because print
#    only shows the number on the screen and then it is lost. With return, the
#    number comes back into my program, so I can keep it in a variable (sum,
#    result) and use it again.


# Your code below

number_1 = 10
number_2 = 20

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)

number_1 = 1
number_2 = 2

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)

number_1 = 4
number_2 = 3

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)


def add_numbers(num1, num2):
    sum_result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum_result)
    return sum_result
    


sum = add_numbers(10, 20)

print(sum)


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = add_numbers(num1, num2)
print("Sum:", result)