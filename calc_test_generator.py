from __future__ import division

import os
import platform
import random
import math
import operator as op
import pickle
from datetime import datetime
from sys import exception
from sympy import Derivative, Integral, pprint, diff, integrate, symbols, log, exp


# this is to choose between the string + and - randomly. then turns it to an operation
def opkey():
    op_key = random.choice(list(rand_ops.keys()))
    return op_key


def main():
    menu = """
Answer calculus topics:
    1. Differentiation
    2. Integral
More actions:
    3. Settings
    4. View score history
    5. Exit
"""
    print(menu)

    ques_type = input("\nChoose the number of what you want to do: ")

    while ques_type != "5":
        os.system(clear)
        if ques_type == "1":
            question(Derivative, diff)
        elif ques_type == "2":
            question(Integral, integrate)
        elif ques_type == "3":
            settings()
        elif ques_type == "4":
            viewscores()
        else:
            print("Input invalid!")

        print(menu)
        ques_type = input("\nChoose the number of what you want to do: ")


# to add more terms
def addterm(term, n):
    terms = [term]
    while n > 1:
        k = random.randint(1, 10)
        n = random.randint(1, n - 1)
        term = k * x**n
        terms.append(term)
    if len(terms) == 1:
        polyn = terms[0]

    # if there are more than 1 term, the random operation will be used
    elif len(terms) == 2:
        polyn = rand_ops[opkey()](terms[0], terms[1])

    elif len(terms) == 3:
        polyn = rand_ops[opkey()](terms[0], terms[1])
        polyn = rand_ops[opkey()](polyn, terms[2])

    elif len(terms) == 4:
        polyn = rand_ops[opkey()](terms[0], terms[1])
        polyn = rand_ops[opkey()](polyn, terms[2])
        polyn = rand_ops[opkey()](polyn, terms[3])

    elif len(terms) == 5:
        polyn = rand_ops[opkey()](terms[0], terms[1])
        polyn = rand_ops[opkey()](polyn, terms[2])
        polyn = rand_ops[opkey()](polyn, terms[3])
        polyn = rand_ops[opkey()](polyn, terms[4])

    return polyn


def polynomial(deg):
    k = random.randint(1, 10)
    n = random.randint(1, deg)
    term = k * x**n

    # call the function that creates another term
    polyn = addterm(term, n)
    return polyn


def question(calculus, solve):
    print("Function types:")

    for a, b in zip(funct_type, range(1, 4)):
        print(f"\t{b}. {a[:1].upper() + a[1:]}")

    print("\t4. All function types\n\t5. Back")
    ftype = input("Choose a function type: ")
    os.system(clear)

    rightorwrong = []

    n = list(difficulty.values())[0]
    difficultylevel = list(difficulty.keys())[0]

    # loop if input not in the option
    while ftype != "5":
        # all questions are polynomial
        if ftype == "1":
            # using for loop to create 10 questions
            for i in range(1, quesnumber[0] + 1):
                print(
                    f"Difficulty: {difficultylevel}\nChosen function type: {funct_type[int(ftype) - 1]} Function"
                )

                # calls the function that creates polynomial
                ques = polynomial(n)

                # prints the terms with derivative symbol and proper exponent
                question = calculus(ques)
                print(f"Question {i} / {quesnumber[0]} \n")
                pprint(question, use_unicode=False)

                # calls the function that prints the answer and other choices
                # if the input is back, the test will end
                choice = choices(ques, solve)
                if choice == "back":
                    break

                rightorwrong.append(choice)
                os.system(clear)

            scorerecord(rightorwrong, calculus)
            os.system(clear)

        # all question are natural log
        elif ftype == "2":
            # using for loop to create 10 questions
            for i in range(1, quesnumber[0] + 1):
                print(
                    f"Difficulty: {difficultylevel}\nChosen function type: {funct_type[int(ftype) - 1]} Function"
                )
                print(
                    "\nNote: In Python, 'log' is the natural logarithm, hence ln =log\n"
                )

                # creates a polynomial to be placed inside ln function
                polyn = polynomial(n - 2)

                # to add more difficulty in the question
                k1 = random.randint(1, n - 1)
                n1 = random.randint(1, n - 2)
                ques = k1 * x**n1 * log(polyn)

                # prints the terms with derivative symbol and proper exponent
                question = calculus(ques)
                print(f"Question {i} / {quesnumber[0]} \n")
                pprint(question, use_unicode=False)

                # calls the function that prints the answer and other choices
                # if the input is back, the test will end
                choice = choices(ques, solve)
                if choice == "back":
                    break

                rightorwrong.append(choice)
                os.system(clear)

            scorerecord(rightorwrong, calculus)
            os.system(clear)

        # all questions are natural exponential
        elif ftype == "3":
            # using for loop to create 10 questions
            for i in range(1, quesnumber[0] + 1):
                print(
                    f"Difficulty: {difficultylevel}\nChosen function type: {funct_type[int(ftype) - 1]} Function"
                )

                # creates a polynomial to be placed on exponential function
                polyn = polynomial(n - 2)

                # to add more difficulty in the question
                k1 = random.randint(1, n - 1)
                n1 = random.randint(1, n - 2)
                ques = k1 * x**n1 * exp(polyn)

                # prints the terms with derivative symbol and proper exponent
                question = calculus(ques)
                print(f"Question {i} / {quesnumber[0]}\n")
                pprint(question, use_unicode=False)

                # calls the function that prints the answer and other choices
                # if the input is back, the test will end
                choice = choices(question, solve)
                if choice == "back":
                    break

                rightorwrong.append(choice)
                os.system(clear)

            scorerecord(rightorwrong, calculus)
            os.system(clear)

        # all function types
        elif ftype == "4":
            for i in range(1, quesnumber[0] + 1):
                ftype = random.choice(funct_type)
                if ftype == funct_type[0]:
                    print(
                        f"Difficulty: {difficultylevel}\nChosen function type: {ftype} Function"
                    )

                    # calls the function that creates polynomial
                    q = polynomial(n)

                elif ftype == funct_type[1]:
                    print(
                        f"Difficulty: {difficultylevel}\nChosen function type: {ftype} Function"
                    )

                    # creates a polynomial to be placed inside ln function
                    polyn = polynomial(n - 2)

                    # to add more difficulty in the question
                    k1 = random.randint(1, n - 1)
                    n1 = random.randint(1, n - 2)
                    q = k1 * x**n1 * log(polyn)

                elif ftype == funct_type[2]:
                    print(
                        f"Difficulty: {difficultylevel}\nFunction type: {ftype} Function"
                    )

                    # creates a polynomial to be placed on exponential function
                    polyn = polynomial(n - 2)

                    # to add more difficulty in the question
                    k1 = random.randint(1, n - 1)
                    n1 = random.randint(1, n - 2)
                    q = k1 * x**n1 * exp(polyn)

                question = calculus(q)
                print(f"Question {i} / {quesnumber[0]} \n")
                pprint(question, use_unicode=False)

                # calls the function that prints the answer and other choices
                # if the input is back, the test will end
                choice = choices(question, solve)
                if choice == "back":
                    break

                rightorwrong.append(choice)
                os.system(clear)

            scorerecord(rightorwrong, calculus)
            os.system(clear)

        else:
            print("Invalid input!")
        print("Function types:")

        # print all function type in the list
        for a, b in zip(funct_type, range(1, 4)):
            print(f"\t{b}. {a}")
        print("\t4. All function types\n\t5. Back")
        ftype = input("Choose a function type: ")
        os.system(clear)


# question is the equation the prgram created
# solve is whether its differentiation or integral
def choices(question, solve):
    letter = ["a", "b", "c", "d"]
    k = random.randint(1, 5)
    n = random.randint(1, 3)
    randomterm = k * x**n
    # sympy can solve an equation
    ans = solve(question)
    choices = [
        ans,
        ans * random.randint(2, 3),
        rand_ops[opkey()](ans, randomterm),
        rand_ops[opkey()]((n + 1) * x, ans),
    ]
    print("\nChoose the letter of the correct answer:\n")

    anslist = {}
    for a, b in zip(letter, random.sample(choices, 4)):
        anslist.update({a: b})
        print(f"{a}.) ")
        pprint(b, use_unicode=False)
        print()

    # list out keys and values separately
    key = list(anslist.keys())
    value = list(anslist.values())

    # makes the answer equal to the letter coresponding it
    anss = key[value.index(ans)]
    u_ans = input(
        "\nType 'back' to return text\nEnter the letter of your answer:  "
    ).lower()
    while u_ans != "back":
        if u_ans in letter:
            check = answer(ans, anss, u_ans)
            return check

        else:
            print("Invalid input!")
            u_ans = input(
                "\nType 'back' to return text\nEnter the letter of your answer: "
            ).lower()
    return u_ans


# checking if the answer is correct
def answer(ans, anss, u_ans):
    response = ["Good job!", "Nice work!", "Excellent!", "Great Work!", "Keep it up!"]
    if u_ans == anss:
        print(f"\n{response[random.randint(0, 4)]} Answer correct.")
        check = "right"
    else:
        print("Answer incorrect.\n")
        check = "wrong"

    print(f"Correct answer:\n{anss}.) ")
    pprint(ans, use_unicode=False)
    _ = input("Press enter to continue.")
    return check


# score recorder
# r_or_w is the list where the user got corrrect and incorrect
# calculus is whether to save it to integration score history or differentiation
def scorerecord(r_or_w, calculus):
    time = datetime.now()
    count = r_or_w.count("right")

    # save score in differentiation score history
    if calculus == Derivative:
        calculus = "Derivative"
        try:
            with open("diff_scores.pickle", "rb") as p:
                diff_total = pickle.load(p)
        except EOFError:
            diff_total = {}

        # update scores after a user finishes answering
        diff_total.update({f"{time}": f"{count} / {quesnumber[0]}"})
        with open("diff_scores.pickle", "wb") as p:
            pickle.dump(diff_total, p)
        # print all score
        print(f"Test done!\nPress enter to exit.\n{calculus} score history:\n")
        for a, b in zip(reversed(diff_total.keys()), reversed(diff_total.values())):
            print(f"{a} -- Score: {b}")
        _ = input()

    # save score in integration score history
    else:
        calculus = "Integral"
        try: 
            with open("integ_scores.pickle", "rb") as p:
                integ_total = pickle.load(p)
        except EOFError:
            integ_total = {}

        # update scores after a user finishes answering
        integ_total.update({f"{time}": f"{count} / {quesnumber[0]}"})
        with open("integ_scores.pickle", "wb") as p:
            pickle.dump(integ_total, p)
        # print all score
        print(f"Test done!\nPress enter to exit.\n{calculus} score history:\n")
        for a, b in zip(reversed(integ_total.keys()), reversed(integ_total.values())):
            print(f"{a} -- Score: {b}")
        _ = input()


def settings():
    print("Welcome to settings!")
    print(
        "1. Clear score history.\n2. Change difficulty.\n3. Change number of questions.\n4. Back"
    )
    setting = input("Choose the number of what action you want:  ")
    os.system(clear)
    while setting != "4":
        # clear the score history
        if setting == "1":
            choose = input(
                "Clear history:\n1. Differentiation\n2. Integral\n3. Both\n4. Cancel\nWhat do you want to clear?  "
            )
            os.system(clear)
            while choose != "4":
                if choose == "1":
                    diff_total = {}
                    with open("diff_scores.pickle", "wb") as p:
                        pickle.dump(diff_total, p)
                    _ = input("Score history cleared.\nPress enter to back.")
                    os.system(clear)

                elif choose == "2":
                    integ_total = {}
                    with open("integ_scores.pickle", "wb") as p:
                        pickle.dump(integ_total, p)
                    _ = input("Score history cleared.\nPress enter to back.")
                    os.system(clear)

                elif choose == "3":
                    diff_total = {}
                    integ_total = {}
                    with open("diff_scores.pickle", "wb") as p:
                        pickle.dump(diff_total, p)
                    with open("integ_scores.pickle", "wb") as p:
                        pickle.dump(integ_total, p)
                    _ = input("Score history cleared.\nPress enter to back.")
                    os.system(clear)

                else:
                    print("Input invalid!")
                choose = input(
                    "Clear history:\n1. Differentiation\n2. Integral\n3. Both\n4. Cancel\nWhat do you want to clear?  "
                )
                os.system(clear)

        # changing difficulty
        elif setting == "2":
            print(
                "Change difficulty:\n\t1. Easy\n\t2. Medium (default)\n\t3. Hard\n\t4. Back"
            )
            difficult = input("Choose new difficulty: ")
            os.system(clear)

            while difficult != "4":
                if difficult == "1":
                    difficulty.clear()
                    difficulty.update({"Easy": 3})
                    print("Difficulty successfully updated to 'Easy'.")
                    _ = input("Enter to back.")
                    os.system(clear)
                elif difficult == "2":
                    difficulty.clear()
                    difficulty.update({"Medium (default)": 5})
                    print("Difficulty successfully updated to 'Medium (Default)'")
                    _ = input("Enter to back.")
                    os.system(clear)
                elif difficult == "3":
                    difficulty.clear()
                    difficulty.update({"Hard": 7})
                    print("Difficulty successfully updated to 'Hard'")
                    _ = input("Enter to back.")
                    os.system(clear)
                else:
                    os.system(clear)
                    print("Input invalid.")
                print(
                    "Change difficulty:\n\t1. Easy\n\t2. Medium (default)\n\t3. Hard\n\t4. Back"
                )
                difficult = input("Choose new difficulty: ")
                os.system(clear)

        # change how many questions
        elif setting == "3":
            print(
                "Change number of questions\n\t1. 5 items\n\t2. 10 items (default)\n\t3. 15 items\n\t4. 20 items\n\t5. Custom\n\t6. Back"
            )
            number = input("Choose how many items you want to answer:  ")
            while not number.isdigit():
                os.system(clear)
                print("Input invalid.")
                print(
                    "Change number of questions\n\t1. 5 items\n\t2. 10 items (default)\n\t3. 15 items\n\t4. 20 items\n\t5. Custom\n\t6. Back"
                )
                number = input("Choose how many items you want to answer:  ")
            quesnumber[0] = int(number) * 5
            print(f"Number of questions successfully changed to {quesnumber[0]} items.")
            _ = input("Press enter to back.")
            os.system(clear)

        else:
            print("Input not valid.\n")

        print("Welcome to settings!")
        print(
            "1. Clear score history.\n2. Change difficulty.\n3. Change number of questions.\n4. Back"
        )
        setting = input("Choose the number of what action you want:  ")
        os.system(clear)


def viewscores():
    print("1. Derivative\n2. Integral\n3. Back")
    view = input("What score history do you want to see?  ")
    os.system(clear)
    while view != "3":
        if view == "1":
            print("Viewing differentiation score history:")
            try:
                with open("diff_scores.pickle", "rb") as p:
                    diff_total = pickle.load(p)
            except EOFError:
                diff_total = {}

            print("Press enter to back.")
            for a, b in zip(
                reversed(list(diff_total.keys())), reversed(list(diff_total.values()))
            ):
                print(f"{a} -- Score: {b}")
            _ = input()
            os.system(clear)
        elif view == "2":
            print("Viewing integrtion score history:")
            try:
                with open("integ_scores.pickle", "rb") as p:
                    integ_total = pickle.load(p)
            except EOFError:
                integ_total = {}

            print("Press enter to back.")
            for a, b in zip(
                reversed(list(integ_total.keys())), reversed(list(integ_total.values()))
            ):
                print(f"{a} -- Score: {b}")
            _ = input()
            os.system(clear)
        else:
            print("Input Invalid.")
        print("1. Derivative\n2. Integral\n3. Back")
        view = input("What score history do you want to see?  ")
        os.system(clear)


if __name__ == "__main__":
    diff_score_file = "diff_scores.pickle"
    if not os.path.exists(diff_score_file):
        open(diff_score_file, 'wb').close()

    integ_score_file = "integ_scores.pickle"
    if not os.path.exists(integ_score_file):
        open(integ_score_file, 'wb').close()

    x = symbols("x")

    user_os = platform.system()
    clear = "cls"

    if user_os == "Linux":
        clear = "clear"

    difficulty = {"medium (default)": 5}
    quesnumber = [10]

    diff_total = {}
    integ_total = {}

    # dictionary for function types
    funct_type = ["polynomial", "natural logarithm", "natural exponent"]

    # dictionary for + and -
    rand_ops = {"+": op.add, "-": op.sub}

    main()
