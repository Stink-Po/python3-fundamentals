# Given an `elapsed` time (in seconds), write code to set a variable `magnitude` based on the following conditions:
#
# - if elapsed time is less than 1 minute, `magnitude` --> `'seconds'`
# - if elapsed time is more than 1 minute, but less than 1 hour, `magnitude` --> `'minutes'`
# - if elapsed time is more than 1 hour, but less than 1 day, `magnitude` --> `'hours'`
# - if elapsed time is more than 1 day, but less than 1 week: `magnitude` --> `'days'`
# - if elapsed time is more than 1 week, `magnitude` --> '`weeks'`

def elapsed_time_calculator(elapsed: int):
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour
    seconds_in_week = 7 * seconds_in_day
    try:
        if elapsed < seconds_in_minute:
            magnitude = 'seconds'
        elif elapsed < seconds_in_hour:
            magnitude = 'minutes'
        elif elapsed < seconds_in_day:
            magnitude = 'hours'
        elif elapsed < seconds_in_week:
            magnitude = 'days'
        else:
            magnitude = 'weeks'
        return magnitude

    except TypeError:
        return f"invalid value"



