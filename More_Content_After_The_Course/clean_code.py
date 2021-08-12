from typing import Union
def calculation (x:Union[int,float],y:Union[int,float]) -> Union[int,float]:
    return (x + y) ** x
print(calculation(3,3))
#print(calculation(3,"x"))

def power(x, y):
    """
    This takes to numbers, the first is the base
     and the second is theexponent
    Args:
        x (float) : This is the base
        y (float) :  This is the exponent
    Returns:
        x ** y (float)
    """
    return x ** y
print(power(3,4))

numbers = list(range(50))
#filtered_list = []
#for number in numbers:
#    if number % 3 == 0 and number % 5 == 0:
#        filtered_list.append(number)
filtered_list = list(filter(lambda x: x % 3 == 0 and x % 5 == 0,numbers))
print(filtered_list)

#cubed = []
#for number in numbers:
#    if number % 10:
#        cubed.append(number ** 3)
cubed = [number ** 3 for number in numbers if number % 10 == 0]
print(cubed)

def filter_list_to_power (power:int,divisor:int, number_of_values: int)->list:
    """
    This takes in a list of a range of numbers starting at zero 
    and returns a filtered list to a given power if the number 
    is divisible by the divisor
    Args:
        power : (int) the power that it is being raised to
        divisor : (int) what is checked to see if the number is divisible by
        number_of_values : (int) the length of the numbers list
    Returns:
        filtered_list : (list)the list of filtered values
    """
    numbers = list(range(number_of_values))
    filtered_list = [number ** power for number in numbers if number % divisor == 0]
    return filtered_list
print(filter_list_to_power(3,6,60))