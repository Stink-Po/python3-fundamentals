# Exercise 1
# Given the following string:
#
# s = 'FfEeDdCcBbAa'
# Create two new variables that contain just the lower and upper case letters of s respectively, in the correct
# alphabetical order, i.e:
#
# 'ABCDEF'
# 'abcdef'
def to_upper(text: str):
    text = text.upper()
    text = sorted(text)
    return "".join(text)


def to_lower(text: str):
    text = text.lower()
    text = sorted(text)
    return "".join(text)

