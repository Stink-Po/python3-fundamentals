# Given the following matrix:

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Make this matrix into an identity matrix (setting the diagonal elements to 1).
#
# Your code should mutate m.
m[0][0], m[1][1], m[2][2] = 1, 1, 1

print(m)
