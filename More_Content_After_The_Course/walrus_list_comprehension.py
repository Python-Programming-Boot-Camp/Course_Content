numList = [2,3,6,5,20,22]

def calculate_result(x):
    return x**3 + 3*x**2

#result = [calculate_result(x) for x in numList if calculate_result(x) < 300]
result = [result for x in numList if (result := calculate_result(x)) < 300]
print(result)