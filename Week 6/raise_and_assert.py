try:
    print("Enter 2 numbers to divide")
    num1 = float(input("What is the first number: "))
    assert num1 > 0
    raise ZeroDivisionError
    num2 = float(input("What is the second number: "))
    print (num1 / num2)
except (ValueError, ZeroDivisionError):
    print("There was either a value or zero division error")