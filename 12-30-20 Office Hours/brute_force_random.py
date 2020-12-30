import random
number = int(input("Input a number that is a password: "))
guess = 0
while (number!=guess):
    guess = random.randint(0,999999)
    #print(guess)
print("Your password is " + str(number))