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

# 1. In: six answers typed by the user about one ads campaign: the channel,
#    the objective, the budget (a number), the result, and two yes/no
#    decisions (keep running it, increase the budget).
# 2. Process: the answers are put in a dictionary. The program reads the
#    channel, adds 20 % to the budget if the answer is yes, removes the
#    increase_budget field with pop() once it is applied, then shows every
#    field with a for loop.
# 3. Out: the channel, the removed field, then every field with its value,
#    one per line, and "not recorded" for a field that does not exist.
# 4. My object, my fields, and why those: an ads campaign review. These are
#    the questions I really answer after a campaign: where it ran, what it was
#    for, how much it cost, what it gave, and what we decide next.


# Your code below

# Ask the user about one ads campaign
# (strip() and lower() so that "Yes", "yes" and " YES " all mean yes)
channel = input("Which channel is the ads campaign on? ")
objective = input("What is the objective? ")
budget = float(input("What is the budget in €? "))
result = input("What was the result? ")
keep = input("Do we keep running it? (yes/no) ").strip().lower()
increase = input("Do we increase the budget? (yes/no) ").strip().lower()

# Put every answer in one dictionary
campaign = {
    "channel": channel,
    "objective": objective,
    "budget": budget,
    "result": result,
    "continue": keep,
    "increase_budget": increase,
}

# Read: show one field
print("The campaign runs on : ", campaign["channel"])

# Change: if we decided to increase the budget, add 20 %
if campaign["increase_budget"] == "yes":
    campaign["budget"] = campaign["budget"] * 1.2

# Remove: the yes/no about the budget is not needed once it is applied
removed = campaign.pop("increase_budget")
print("Removed field increase_budget, its value was : ", removed)

# Display every field with its value
for field, value in campaign.items():
    print(field, ":", value)

# A field that does not exist: .get() shows a message instead of crashing
print("start_date :", campaign.get("start_date", "not recorded"))

# Check: campaign["start_date"] -> ... (the error), the program stopped.
# Fix: campaign.get("start_date", "not recorded") -> "not recorded", no crash.
# Run with "yes" for the budget: 1000 became ... / with "no": it stayed ...