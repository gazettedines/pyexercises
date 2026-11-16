# ==============================================================
# SURVIVE THE QUARTER - Croissant Rocket
# Name:  Thi Thanh Lam NGUYEN
# Group: C   (scenario file: scenarios_C.csv)
# ==============================================================
#
# 1. WHAT GOES IN?
#    - my file is scenarios_C.csv
#    - the columns are separated by commas
#    - there are 14 columns: Event, Day, Decision, Repution, Budget and Outcome, three times each (1, 2, 3)
#    - the numbers are text with a unit, like "+15pts" or "-500 EUR" so I need to remove "pts" and "EUR" before I use int()
#    - option B is in all the columns with the number 2
#
# 2. WHAT HAPPENS? (one day)
#    - show the day, the budget and the reputation
#    - show the situation and A, B, C
#    - ask the player to choose, again if the answer is wrong
#    - change the budget and the reputation, show the result
#    - if one gauge is 0 or less, the player is fired
#
# 3. WHAT COMES OUT?
#    At the end the player sees "fired" and why, or the score and
#    the title. Then the best move and the worst move.
#    One line of results.csv: Thanh,5900,70,Growth Hacker,2026-11-16
#
# 4. WHAT COULD GO WRONG?
#    - The player types a wrong letter: the game asks again.
#    - The reputation goes above 100: I keep it at 100.
#    - A gauge goes to 0 or less: the game stops at once.
#    - The CSV file is missing: the game shows a message, no crash.
#
# FEATURE CHOSEN: c) High score
#    At the end, I read results.csv and say if the player beat the
#    best budget of all the previous games (only when the player
#    survived: a fired player gets no high score). I chose it because it
#    makes me read an external file a second time (results.csv),
#    so I practise reading AND writing, and it gives players a
#    reason to play again.
# ==============================================================

import csv
import os
import random
import sys
from datetime import date

# Settings of the game (from the brief). The two files are looked for
# in the same folder as this script, so the game also works when it is
# started from another folder.
FOLDER = os.path.dirname(os.path.abspath(__file__))
SCENARIO_FILE = os.path.join(FOLDER, "scenarios_C.csv")
RESULTS_FILE = os.path.join(FOLDER, "results.csv")
START_BUDGET = 10000
START_REPUTATION = 50
MAX_REPUTATION = 100
DAYS = 10
LETTERS = ["A", "B", "C"]


# Read what the player types. If the player presses Ctrl+C or
# Ctrl+D, input() raises an error: I stop the game nicely instead.
def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. See you next quarter!")
        sys.exit(0)


# Turn a text like "+15 pts" or "-800 EUR" into a number (15, -800).
# I remove the units, the spaces and the commas, then use int().
def to_number(text):
    cleaned = text.replace("pts", "").replace("EUR", "")
    cleaned = cleaned.replace(",", "").replace(" ", "").strip()
    return int(cleaned)


# Open the scenario file with the csv module and build a list.
# Each scenario is a dictionary with the event and a list of 3
# options. Each option is a tuple:
# (text, budget_change, reputation_change, feedback)
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                options = []
                for i in range(1, 4):
                    option = (
                        row["Decision " + str(i)].strip(),
                        to_number(row["Budget " + str(i)]),
                        to_number(row["Reputation " + str(i)]),
                        row["Outcome " + str(i)].strip(),
                    )
                    options.append(option)
                scenarios.append({"event": row["Event"].strip(), "options": options})
            except (KeyError, ValueError, AttributeError):
                # broken line: skip it, keep the rest of the file
                continue
    return scenarios


# Ask the player's name. Empty name -> "Player".
def ask_name():
    name = safe_input("What is your name, new marketing manager? ").strip()
    if name == "":
        name = "Player"
    return name


# Show the day number, the two gauges, the situation and A, B, C.
def show_day(day, budget, reputation, scenario):
    print()
    print("--- Day " + str(day) + " ---")
    print("[Budget: " + str(budget) + " EUR | Reputation: "
          + str(reputation) + "/" + str(MAX_REPUTATION) + "]")
    print(scenario["event"])
    for i in range(3):
        print("   " + LETTERS[i] + ": " + scenario["options"][i][0])


# Ask A, B or C again and again until the answer is valid.
# Returns the position of the option in the list (0, 1 or 2).
def ask_choice():
    answer = safe_input("Your choice (A, B or C): ").strip().upper()
    while answer not in LETTERS:
        answer = safe_input("Please type A, B or C: ").strip().upper()
    return LETTERS.index(answer)


# Apply the impact of the chosen option to the two gauges.
# Reputation can never go above 100. Returns a tuple (budget, reputation).
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = reputation + reputation_change
    if reputation > MAX_REPUTATION:
        reputation = MAX_REPUTATION
    return budget, reputation


# Give the title that matches the final score (table of the brief).
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Show the best and the worst move. The history is a list of tuples
# (reputation_change, day, text). Python compares tuples starting
# with the first element, so max() and min() use the reputation change.
def show_best_and_worst(history):
    if len(history) == 0:
        return
    best_change, best_day, best_text = max(history)
    worst_change, worst_day, worst_text = min(history)
    print('Best move:  day ' + str(best_day) + ', "' + best_text
          + '" (' + format(best_change, "+d") + ")")
    print('Worst move: day ' + str(worst_day) + ', "' + worst_text
          + '" (' + format(worst_change, "+d") + ")")


# FEATURE c: read results.csv and find the best budget of all the
# games played before. Returns None if there is no previous game.
def read_best_budget(filename):
    if not os.path.exists(filename):
        return None
    best = None
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # games where the player was fired do not count
            if row.get("title") == "Fired":
                continue
            try:
                value = int(row["budget"])
            except (KeyError, ValueError, TypeError):
                continue
            if best is None or value > best:
                best = value
    return best


# FEATURE c: say if the player beat the best budget.
def show_high_score(budget, best_budget):
    if best_budget is None:
        print("First game in results.csv: your budget is the high score!")
    elif budget > best_budget:
        print("NEW HIGH SCORE! You beat the best budget ("
              + str(best_budget) + " EUR).")
    else:
        print("The best budget is still " + str(best_budget)
              + " EUR. Try again!")


# Add one line at the end of results.csv: name, budget, reputation,
# title, date. If the file does not exist, I write the header first.
def save_result(filename, name, budget, reputation, title):
    new_file = not os.path.exists(filename)
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# The main game: load, shuffle, play 10 days, then the end screen.
def play_game():
    # load the file, or stop with a clear message if it is missing
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print("Error: scenarios_C.csv was not found. Put it in the "
              "same folder as survive_the_quarter.py.")
        return
    if len(scenarios) == 0:
        print("Error: no valid scenario in scenarios_C.csv.")
        return

    print("Welcome to Croissant Rocket, croissants delivered by drone!")
    name = ask_name()
    budget = START_BUDGET
    reputation = START_REPUTATION
    history = []
    fired_reason = ""

    # shuffle the scenarios and keep 10 of them (or fewer if the file is short)
    random.shuffle(scenarios)
    days_to_play = scenarios[:DAYS]

    # one loop turn = one day
    day = 0
    for scenario in days_to_play:
        day = day + 1
        show_day(day, budget, reputation, scenario)
        index = ask_choice()
        option = scenario["options"][index]
        text, budget_change, reputation_change, feedback = option

        budget, reputation = apply_choice(budget, reputation, option)
        print(feedback)
        print("Budget " + format(budget_change, "+d") + " EUR, Reputation "
              + format(reputation_change, "+d"))

        history.append((reputation_change, day, text))

        # check the two gauges: fired at once if one is at 0 or less
        if budget <= 0 and reputation <= 0:
            fired_reason = "you have no money AND no reputation left"
        elif budget <= 0:
            fired_reason = "the budget is empty, the bank says no"
        elif reputation <= 0:
            fired_reason = "your reputation hit zero, the internet hates you"
        if fired_reason != "":
            break

    # end of the game: read the high score BEFORE saving this game
    best_budget = read_best_budget(RESULTS_FILE)
    print()
    print("=" * 30)
    if fired_reason != "":
        title = "Fired"
        print("You are FIRED on day " + str(day) + ": " + fired_reason + ".")
        print("Budget: " + str(budget) + " EUR, reputation: "
              + str(reputation) + "/" + str(MAX_REPUTATION))
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Quarter survived!")
        print("Budget left: " + str(budget) + " EUR, reputation: "
              + str(reputation) + "/" + str(MAX_REPUTATION))
        print("Final score: " + str(score))
        print(name + ", your title: " + title)
    print()
    show_best_and_worst(history)
    # a fired player cannot hold the high score
    if fired_reason == "":
        show_high_score(budget, best_budget)

    save_result(RESULTS_FILE, name, budget, reputation, title)
    print("Saved in results.csv")


# Start the game only when the file is run directly
if __name__ == "__main__":
    play_game()
