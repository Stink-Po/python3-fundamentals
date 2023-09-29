# Using two types of string interpolation, and given the variable `a` that contains an integer, print out the
# following string for `a`:
#
# `The number ...value of a... is (or is not) even`
#
# For example, if `a` is `42`, the code should print:
#
# `'The number 42 is even'`
#
# But if `a` is `31`, then the **same** code should print:
#
# `'The number 31 is not even'`

def number_printer_one(num: int):
    if num % 2 == 0:
        result = "even"
    else:
        result = "odd"

    print("Output with .format method : The number {} is {} ".format(num, result))
    print(f"Output with fstring method : The number {num} is {result}")


