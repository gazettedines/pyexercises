"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. One dictionary written in the code: a
#    marketing campaign with 5 fields (name, channel, budget, start date, target).
# 2. Process: the program reads one field, changes the budget, adds the clicks,
#    removes the start date, then goes through every field with a for loop.
# 3. Out: the campaign name, then every field with its value, one per line,
#    and a message for a field that does not exist.
# 4. My object, my five fields, and why those: a marketing campaign. Name and
#    channel to know which campaign it is and where it runs, budget to control
#    the cost, start date to plan it, and target to know who it speaks to.


# Your code below
# A real marketing campaign described with 5 fields
campaign = {
    "name": "Winter Sale",
    "channel": "E-commerce",
    "budget": 4000,
    "start_date": "2026-12-01",
    "target": "Students 18-25",
}

# Read: show one field
print("Campaign name:", campaign["name"])

# Change: the budget goes up, and I add a new field for the clicks
campaign["budget"] = 4500
campaign["clicks"] = 1200

# Remove: the start date is no longer needed once the campaign has started
del campaign["start_date"]

# Display every field with its value
for field, value in campaign.items():
    print(field, ":", value)

# Ask for a field that does not exist, without crashing:
# .get() gives a default message instead of an error
print("Conversions:", campaign.get("conversions", "not recorded"))