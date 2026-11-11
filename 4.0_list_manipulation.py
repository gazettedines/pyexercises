"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by user. Two lists written in the code: 8 marketing channels 
#    (text) and the budget of each channel in € (numbers), in the same order 
# 2. Process: the program shows the list, picks one channel by its position, sorts 
#    the channels in alphabetical order, then counts the channels and computes the 
#    total budget and the biggest budget with len(), sum() and max()
# 3. Out: on the screen, the whole list, one chosen channel with its budget, 
#    the sorted list, the number of channels, the total budget and the biggest budget
# 4. What my list is about, and what I computed from it: the marketing channels of a 
#    brand and their budgets. I computed the total budget, to know how much the whole 
#    plan costs, and the biggest budget, to see which channel takes the most money 
#    and if it is worth it


# Your code below
# My marketing channels, and the budget of each one (in €), in the same order
channels = ["Social media", "Modern trade", "General trade", "E-commerce",
            "Email marketing", "Search ads", "TV", "KOL marketing"]
budgets = [3000, 2500, 1800, 4000, 600, 2200, 5000, 1500]

# Show the whole list
print("All channels:", channels)

# One item I chose: e-commerce, because ...
print("Chosen channel:", channels[3], "-", budgets[3], "€")

# The list sorted in alphabetical order
print("Sorted:", sorted(channels))

# Computed: how many channels, the total budget, and the biggest budget
print("Number of channels:", len(channels))
print("Total budget:", sum(budgets), "€")
print("Biggest budget:", max(budgets), "€")