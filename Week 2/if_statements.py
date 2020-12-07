print("Enter 3 numbers to see what is the largest")
num1 = float(input("What is the first number: "))
num2 = float(input("What is the first number: "))
num3 = float(input("What is the first number: "))
if (num1>=num2 and num1>=num3):
    largest_number = num1
elif (num2>=num1 and num2>=num3):
    largest_number = num2
else:
    largest_number = num3
print("The largest number is " + str(largest_number))    