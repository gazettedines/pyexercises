"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my two lists from exercise 4.0, written in the code: 8 marketing
#    channels and the budget of each one in €.
# 2. Process: the program computes the total budget once, then goes through
#    every channel with a for loop and computes its share of the total in %.
# 3. Out: 8 lines, one per channel: its position, its name, its budget and
#    its share of the total budget.
# 4. What I compute for each item, and why it is worth showing: the share of
#    the total budget. The reader sees at once which channels take most of the
#    money, and can ask if those are really the best channels.


# Your code below
# My two lists from exercise 4.0, in the same order
channels = ["Social media", "Modern trade", "General trade", "E-commerce",
            "Email marketing", "Search ads", "TV", "KOL marketing"]
budgets = [3000, 2500, 1800, 4000, 600, 2200, 5000, 1500]

# The total budget, computed once before the loop
total = sum(budgets)

# For every channel: its position (starting at 1), its name, its budget,
# and its share of the total budget in %
for i in range(len(channels)):
    share = budgets[i] / total * 100
    print(i + 1, channels[i], ":", budgets[i], "€ =", round(share, 1), "% of the budget")