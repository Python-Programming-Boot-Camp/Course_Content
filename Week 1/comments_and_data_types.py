# This is a comment. The python Interpreter doesn't read this
# There are 4 main types of data types string, int, float, boolean

# the default for input is a string
name = input("What is your name: ")

# in order to make an input another data type you must convert it
age = int(input("What is your age: "))  # You can have an inline comment like this

# The print statement can only take in strings. Here are 2 options
print("Hello " + name + " you are " + str(age))
print("Hello", name, "you are", age)
