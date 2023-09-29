# Given two floats a and b, and some tolerance tol, write an expression that will test whether a and b are within tol
# of each other.

# my solution ->
def tolerance_calculator(a: float, b: float, tolerance: float) -> None:
    difference = abs(a - b)
    print(difference)
    print(difference < tolerance)


