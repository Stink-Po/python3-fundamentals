# You are given a list of tuples that each contain 4 values:
#
# ```
# (amount, currency, target_currency, exchange_rate)
# ```
#
# data = [
#    (100, 'USD', 'EUR', 0.83),
#    (100, 'USD', 'CAD', 1.27),
#    (100, 'CAD', 'EUR', 0.65)
# ]
# Write code that converts the `amount` from its `currency` to its `target_currency` using the `exchange_rate` (which
# is the exchange rate for `1` `currency` in `target_currency`).
#
# Try to make your code as generic as possible (we'll see later how to use loops, so we don't have to write three
# separate statements).
#
# In other words, you'll need three blocks of code here that are essentially almost identical.
#
# Use unpacking to assign the values in each tuple to variables.
#
# Your result for each row should print something like this out:
#
# ```
# 100 USD = 83 EUR
# ```

def exchange_currency(currency: str, target: str, amount: int):
    data = [
        (100, 'USD', 'EUR', 0.83),
        (100, 'USD', 'CAD', 1.27),
        (100, 'CAD', 'EUR', 0.65)
    ]
    output = None
    for row in data:
        if row[1] == currency:
            if row[2] == target:
                currency_tuple = row
                output = amount * currency_tuple[3]
    else:
        print("invalid currency or target")

    return output


