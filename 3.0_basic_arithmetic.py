"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers typed by the user. input() gives text, so int() turns each answer 
#    into a whole nummber
# 2. Process: the program computes the sum, the difference, the product and the division
#    of the two numbers. Before dividing, it checks that the second number is 
#    not zero
# 3. Out: on the screen, the two numbers, the four results: sum, diff, product, 
#    division (or a message if the second number is zero)
# 4. What happens when the second number is zero, and why: my program shows the message 
#    "The second number is zero" instead of a result, because the other three 
#    calculations still yield the correct results, the user doesn't lose them.


# Your code below
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number:"))

print("The first number is : ", number_1)
print("The second number is : ", number_2)

# Sum of two number
sum = number_1 + number_2
print("The sum of two numbers is: ", sum)

# Difference of two numbers
diff = number_1 - number_2
print("The diff of two numbers is: ", diff)

# produt of two numbers
product = number_1 * number_2
print("The product of two numbers is:", product)

# division of two numbers

if number_2 != 0:
    division = number_1 / number_2
    print("The division of two numbers is:", division)
else:
    print("The second number is zero")
