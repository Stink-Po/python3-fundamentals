# Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`, and leave `a` unchanged
# otherwise. Use an `if...else...` statement. with Ternary Operator
def test_value(a):
    return "N/A" if a is None else a
