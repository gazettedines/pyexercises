"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: names of marketing channels typed by the user, one per question,
#    or the word "stop".
# 2. Process: a while loop asks again and again. Each answer is cleaned with
#    strip() and lower(). If it is "stop", the loop ends with break. Otherwise
#    the channel is added to a list. The loop also ends after 5 questions.
# 3. Out: a message saying why the loop ended, then a summary: the number of
#    attempts, the number of channels added, and the list of new channels.
# 4. My stop condition, my attempt limit, my summary: the loop stops when the
#    user types "stop" (with any capitals or spaces, because a user often types
#    "Stop" or adds a space by mistake), or after 5 attempts, because a plan
#    with too many new channels is hard to manage. The summary shows the
#    attempts, how many channels were added, and which ones.


# Your code below
# The channels the user adds during the loop, and the safety limit
added = []
max_attempts = 5
attempts = 0

# Keep asking until the user types "stop" or the limit is reached
while attempts < max_attempts:
    answer = input("Add a channel (or type stop): ")
    attempts += 1

# Clean the answer: remove spaces at both ends and use small letters,
    # so "Stop", "stop" and " STOP " all mean the same thing
    if answer.strip().lower() == "stop":
        print("You stopped the loop.")
        break

    # Otherwise, keep the channel name
    added.append(answer.strip())

# If the loop ended because of the limit, say it
if attempts == max_attempts and len(added) == max_attempts:
    print("Limit reached: you can add", max_attempts, "channels at most.")

# Summary of what happened
print("Attempts:", attempts)
print("Channels added:", len(added))
print("Your new channels:", added)