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
# My list from exercise 4.0
channels = ["Social media", "Modern trade", "General trade", "E-commerce",
            "Email marketing", "Search ads", "TV", "KOL marketing"]

# 1. Alphabetical order: sorted() gives a NEW list, the original does not move
print("A to Z:", sorted(channels))

# 2. Reverse alphabetical order: also a new list
print("Z to A:", sorted(channels, reverse=True))

# 3. The original order backwards: [::-1] makes a reversed copy
print("Backwards:", channels[::-1])

# 4. Shortest name first: .sort() changes the list IN PLACE,
#    so I use it on a copy, never on the original
copy = channels.copy()
copy.sort(key=len)
print("Shortest first:", copy)

# Proof: the original list is still in the same order as in 4.0
print("Original:", channels)