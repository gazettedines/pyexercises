"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the number of conversions of a campaign, typed by the user (text).
# 2. Process: the program tries to turn the answer into a number with float(),
#    then divides the budget by it to get the cost per acquisition (CPA).
#    Each failure is caught separately. A wrong answer is asked again, up to
#    3 attempts. Zero conversions ends the question, because asking again
#    would give the same 0.
# 3. Out: the CPA in €, or a clear message saying why there is no CPA.
#    The program always ends normally, it never crashes.
# 4. The two failures, and whether they deserve the same message: no.
#    - ValueError: the user typed text or nothing. It is a typing mistake,
#      so I explain and ask again.
#    - ZeroDivisionError: the user typed 0. The answer is correct, the
#      campaign really has no conversions, so I say there is no CPA and stop.
#    Why catch them separately: each failure needs its own message and its own
#    action. Catching every error at once would give the same answer to both,
#    and would also hide other errors I did not expect, like a typo in my code.

# Check:
# - 120 -> "Cost per acquisition (CPA): 33.33 €", then finished normally.
# - 0 -> "0 conversions: the campaign sold nothing...", finished normally.
# - "abc" -> "This is not a number: 'abc'..." and asked again. After 3 times:
#   "Too many wrong answers, I stop here."
# - empty line -> "This is not a number: ''..." and asked again, same as abc.
# None of the four runs stopped the program with an error.

# Your code below

# The campaign budget, and how many wrong answers I accept
BUDGET = 4000
MAX_ATTEMPTS = 3
attempts = 0
cpa = None

# Ask until we have a CPA, or until the attempts are used up
while attempts < MAX_ATTEMPTS and cpa is None:
    attempts += 1
    answer = input("How many conversions did the campaign get? ")

    # Try the risky part: turning text into a number, then dividing
    try:
        conversions = float(answer)
        cpa = BUDGET / conversions

    # Failure 1: not a number (text or empty line) -> explain and ask again
    except ValueError:
        print("This is not a number:", repr(answer), "- please type digits, for example 120.")

    # Failure 2: zero conversions -> no CPA possible, asking again is useless
    except ZeroDivisionError:
        print("0 conversions: the campaign sold nothing, so there is no cost per acquisition.")
        break

# Show the result, or why there is none
if cpa is not None:
    print("Cost per acquisition (CPA):", round(cpa, 2), "€")
elif attempts == MAX_ATTEMPTS:
    print("Too many wrong answers, I stop here.")

print("Program finished normally.")
