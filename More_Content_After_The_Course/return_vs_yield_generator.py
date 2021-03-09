def square(n):
    a = n * n
    #return a
    yield a
    yield 1000
answer = square(2)
print(answer.__next__())
print(next(answer))
#print(next(answer))
answer2 = square(3)
for i in answer2:
    print(i)