# Do the same problem as Exercise 3, but do **not** mutate `m`.

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Copying m in this way we don't modify the original matrix
output = m.copy()

output[0][0], output[1][1], output[2][2] = 1, 1, 1
print(m)
print(output)
