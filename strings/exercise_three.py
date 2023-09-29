# You are given two variables `a` and `b` (with `b` non-zero), and you need to generate a string that reads something
# like this:
#
# ```
# 'a / b = (result)'
# ```
# But you want your string to be nicely formatted for display purposes, so you want to limit displaying possible digits
# after the decimal point in all your values to 4 digits.
def print_value(a: int, b: int):
    print(f"{a} / {b} = {round(a / b, 4)}")
