# key value pairs
phone_numbers = {"doctor":1234567890,"electrician":8000000011}
print(phone_numbers["doctor"])
print(phone_numbers)
for key in phone_numbers.keys():
    print (key, "->", phone_numbers[key])
phone_numbers["doctor"] = 8880000088
print(phone_numbers)
phone_numbers["author"] = 4567890123
print(phone_numbers)
del phone_numbers["author"]
print(phone_numbers)
print(len(phone_numbers))