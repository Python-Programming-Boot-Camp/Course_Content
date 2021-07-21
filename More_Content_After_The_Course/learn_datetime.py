from datetime import datetime, timedelta
current_date = datetime.now()
one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Today: " + str(current_date))
print("Yesterday: " + str(yesterday))
favorite_day = input("Enter your favorite day (mm/dd/yyyy): ")
favorite_day = datetime.strptime(favorite_day,"%m/%d/%Y")
print(favorite_day)
print("Year: " + str(favorite_day.year))
print("Month: " + str(favorite_day.month))
print(favorite_day.strftime("%A, %B %d, %Y"))
time1 = "11:43:02"
time2 = "11:56:01"
time1 = datetime.strptime(time1,"%H:%M:%S")
time2 = datetime.strptime(time2,"%H:%M:%S")
print(time2 - time1)