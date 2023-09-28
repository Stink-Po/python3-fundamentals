# integers in python are whole numbers like :
integer_number = 100
print(integer_number)
integer_number = -100
print(integer_number)
integer_number = 10_000_000
print(integer_number)

# you can also get integer as result of some calculation(expression)

integer_number = 1 + 1
print(integer_number)

# floats in python are floating point numbers the float type used to represent read numbers (floating point)
float_number = 1.0
print(float_number)
float_number = -0.1
print(float_number)
float_number = 3.18
print(float_number)
float_number = 1_000.578_123
print(float_number)
# float representations
float_number = 1.234
print(float_number == 1 + (2 / 10) + (3 / 100) + (4 / 1000))
a = format(0.1 + 0.1 + 0.1, ".25f")
b = format(0.3, ".25f")
print(a == b)
print(a)
print(b)

difference = abs((0.1 + 0.1 + 0.1) - 0.3)
print(difference < 0.0001)
