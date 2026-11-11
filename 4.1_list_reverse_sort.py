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
#    [::-1] make new lists and leave the original alone. .sort() changes a list
#    in place, so I use it only on a copy.
# 3. Out: four lines with the list in four orders, then the original list on
#    the last line, to prove it has not moved.
# 4. My four orders, and which one modifies the list: A to Z, Z to A,
#    backwards, and shortest name first. Only .sort() modifies a list in place
#    (like .reverse() and .pop()), so I used it on a copy, not on the original.


# Your code below

# My list from exercise 4.0, in its original order
channels = ["Social media", "Modern trade", "General trade", "E-commerce",
            "Email marketing", "Search ads", "TV", "KOL marketing"]

# 1. A to Z: sorted() returns a NEW list, the original does not move
print("A to Z         : ", sorted(channels))

# 2. Z to A: sorted() with reverse=True, also a new list
print("Z to A         : ", sorted(channels, reverse=True))

# 3. Backwards: [::-1] makes a reversed copy of the original order
print("Backwards      : ", channels[::-1])

# 4. Shortest name first: .sort() changes a list IN PLACE,
#    so I make a copy first and sort only the copy
copy = channels.copy()
copy.sort(key=len)
print("Shortest first : ", copy)

# Proof: the last line shows the original list, still in the same order as in 4.0
print("Original       : ", channels)

# Check: the last line is the same as my list in 4.0, item by item -> yes / no
# Test: when I wrote channels.sort(key=len) instead of using the copy,
#       the last line changed to: ...