income = float(input("Enter the annual income: "))

if (income <= 85528):
    tax = (income * .18) - 556.02
else:
    additionalIncome = income - 85528
    tax = (additionalIncome * 0.32) + 14839.02
if (tax < 0):
    tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")