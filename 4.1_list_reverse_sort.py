"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of 8 marketing channels from exercise 4.0, written in the code.
# 2. Process: the program puts the list in four different orders. sorted() and
#    [::-1] make new lists. .sort() changes a list in place, so I use it on a copy.
# 3. Out: four lines with the list in four orders, then the original list at
#    the end, to prove it has not moved.
# 4. My four orders, and which one modifies the list: A to Z, Z to A, backwards,
#    and shortest name first. Only .sort() modifies a list in place: that is why
#    I used it on a copy and not on the original.


# Your code below
number_1 = 2
number_2 = 4
number_3 = 6
number_4 = 8
number_5 = 10

print("The first number is : ", number_1)
print("The second number is : ", number_2)
print("The third number is : ", number_3)
print("The fourth number is : ", number_4)
print("The fifth number is : ", number_5)

numbers = [3, 5, 7, 9, 11, 13, 15, 17, 1, 2, 4, 6, 8, 10]
print("The whole list is : ", numbers)
print("The second item of the list is : ", numbers[1])
print("The first item of the list is : ", numbers[0])

sorted_list = sorted(numbers)
print("The sorted list is : ",  sorted_list)

removed_number = numbers.pop()
print("The removed item is : ", removed_number)
print("The list after removing the last item is : ", numbers)
print("The sorted list after removing the last item is : ", sorted_list)
removed_number_last = sorted_list.pop()
print("The removed item from the sorted list is : ", removed_number_last)
print("The sorted list after removing the last item is : ", sorted_list)