# Question 1
# Write some code that generates an `m` x `n` multiplication table.
#
# For example if `m=3` and `n=4` your output should look something like:
#
# ```
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# ---------------
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# ---------------
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# ---------------
# ```

# Your code should be generic enough that it can handle any positive integer values of `m` and `n`.

def create_table(m: int, n: int):
    output = []
    for x in range(1, m + 1):
        inner_output = []
        for y in range(1, n + 1):
            num_str = f"{x} X {y} = {x * y}"
            inner_output.append(num_str)
        output.append(inner_output)
    return output


# Question 2
# You are given the following tuple of lists:
sample_data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)


# Your program should:
# 1. Mutate the lists in `data` to add one more element indicating the distance between the two
#    integer numbers (i.e. the absolute value fo the difference)
# 2. Determine on which date this newly calculate value
#    was the largest.
# 3. Be able to work for a `data` set containing any number of lists.

def calculate(data: tuple):
    for item in data:
        diff = abs(item[-1] - item[-2])
        item.append(diff)
    max_diff = 0
    max_date = ""
    for item in data:
        if item[-1] > max_diff:
            max_diff = item[-1]
            max_date = item[0]
    print(f"Max difference: {max_diff} date is : {max_date}")


# Question 3
# You are given a list of lists containing two numbers that will need to be color coded later based on a
# trend determined by the following rules:
# 1. If the first number of a row is higher than the second number of the
# previous row, append the string `up` to the row
# 2. If the first number of a row is lower than the second number of
# the previous row, append the string `down` to the row
# 3. Otherwise, append `same` to the row.
#
# Obviously you cannot apply these rules to the first row (there is no preceding row), so append an empty string for
# the first row.
#
# Basically think of this as a list of Open/Close values, and we want to assign the values `same`, `up`,
# or `down` based on how a row's Open value compares to the Close of the *previous* row.

# For example, given the following list:
data_example = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]


# Then after your code finishes running, your `data` should look like this:


# [
#     [10, 20, ''],
#     [20, 30, 'same'],
#     [35, 50, 'up'],
#     [45, 60, 'down']
# ]
#
def predict(data: list):
    for idx, (op, cl) in enumerate(data):
        if idx == 0:
            data[idx].append('')
        else:
            prev_op, prev_cl, trend = data[idx - 1]
            if op > prev_cl:
                data[idx].append('up')
            elif op < prev_cl:
                data[idx].append('down')
            else:
                data[idx].append('same')

    return data
