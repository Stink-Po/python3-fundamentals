# Exercise 2
# Concatenate the following tuples into a single one, but replacing the odd values with zeros (0).
#
t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17


# You can assume that every tuple is a sequence of consecutive integers starting with an odd integer.
#
# Try to write your code to be as generic as possible.

def concatenated(tuple1: tuple, tuple2: tuple, tuple3: tuple):
    output_list = []
    for i in tuple1:
        if i % 2 == 0:
            output_list.append(i)
        else:
            output_list.append(0)

    for _ in tuple2:
        if _ % 2 == 0:
            output_list.append(_)
        else:
            output_list.append(0)

    for item in tuple3:
        if item % 2 == 0:
            output_list.append(item)
        else:
            output_list.append(0)

    print(output_list)

    return tuple(output_list)


