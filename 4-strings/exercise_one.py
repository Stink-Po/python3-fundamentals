# Given this string of comma separated characters, create three new variables containing the unicode codepoint
# (in hex), uppercase and lower case versions of each character (also comma delimited).
#
# For example, if the string was `'a, B, c'` you should generate three lists that look like:
# * `['0x61', '0x62', '0x63']`
# * `['a', 'b', 'c']`
# * `['A', 'B', 'C']`
#
# [You should use the `split()` and `strip()` functions, amongst others, to help you solve this.]

s = 'Π, ύ, θ, ω, ν'

characters_list = [item.lstrip() for item in s.split(",")]

hex_list = [hex(ord(item)) for item in characters_list]

lower_list = [item.lower() for item in characters_list]

upper_list = [item.upper() for item in characters_list]


