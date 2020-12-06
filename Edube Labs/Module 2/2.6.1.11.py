hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins= mins + dura
new_hour =mins//60
hour += new_hour
hour %= 24
mins %= 59
print(hour,":",mins)