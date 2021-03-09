def power(n):
    #x = []
    for i in range(10000):
        yield n**i
        #x.append(n**i)
    #return x
answer = power(3)
print(next(answer))
print(next(answer))
print(next(answer))
print(next(answer))