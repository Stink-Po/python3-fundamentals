# Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`, and leave `a` unchanged
# otherwise. Use an `if...else...` statement.

def test_value(a):
    if a is None:
        a = "N/A"
        return a
    else:
        return a
