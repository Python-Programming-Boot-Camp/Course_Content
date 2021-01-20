try:
    print("Enter 2 numbers to divide")
    num1 = float(input("What is the first number: "))
    num2 = float(input("What is the second number: "))
    print (num1 / num2)
except ValueError:
    print("You needed to input a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Something else went wrong")
finally:
    print("This will always print")