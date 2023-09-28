# Given a credit score `score`, assign a string value to another variable `rating` based on the following
# scale:

# - [0, 580) --> Poor
# - [580, 670) --> Fair
# - [670, 740) --> Good
# - [740, 800) --> Very Good
# - [800, 850] --> Excellent


def calculate_credit_score(score: int):
    try:
        if 0 < score <= 580:
            print("Credit Score  is  Poor")
        elif 580 < score <= 670:
            print("Credit Score is Fair")
        elif 670 < score <= 740:
            print("Credit Score is Good")
        elif 740 < score <= 800:
            print("Credit Score is Very Good")
        elif 800 < score <= 850:
            print("Credit Score is Excellent")
        else:
            print("Invalid Score Number")
    except TypeError:
        print("We Expect integer as value")


