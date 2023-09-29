# Exercise 2
# Concatenate the following tuples into a single one, but replacing the odd values with zeros (0).
#
t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17


# You can assume that every tuple is a sequence of consecutive integers starting with an odd integer.
#
# Try to write your code to be as generic as possible.

def concatenated(*args: tuple):
    output_list = []
    for tup in args:
        if isinstance(tuple, tup):
            for item in tup:
                if item % 2 == 0:
                    output_list.append(item)
                else:
                    output_list.append(0)

    return tuple(output_list)
