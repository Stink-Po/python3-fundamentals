# Assume you have some variable elapsed that contains elapsed time in seconds.
# Create three new variables: hours, minutes and seconds, that represent the number of hours, minutes and seconds
# represented by elapsed.
# For example, if elapsed = 7835, then hours = 2, minutes = 10 and seconds = 35

# my solution ->
def calculate_time(elapsed: int) -> None:
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    remaining = (elapsed % 3600) % 60
    print(f"hours : {hours}, minutes: {minutes}, seconds: {remaining}")



