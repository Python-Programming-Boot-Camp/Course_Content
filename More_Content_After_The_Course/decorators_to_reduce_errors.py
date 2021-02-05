def check(func):
    def inner(hours_per_week):
        if hours_per_week < 0:
            print("Hours must be positive")
            return
        return func(hours_per_week) 
    return inner

@check
def hours_per_day(hours_per_week):
    return hours_per_week / 7

#hours_per_day = check(hours_per_day)

print(hours_per_day(21))