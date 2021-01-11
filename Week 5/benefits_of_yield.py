def squares(numbers):
    squared = []
    for i in range (len(numbers)):
        squared.append(numbers[i]**2)
    return squared
print(squares([3,2,5,8]))
def squared(numbers):
    for i in range (len(numbers)):
        yield numbers[i]**2
print(list(squared([3,2,5,8])))