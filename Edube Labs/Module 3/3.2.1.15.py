c0 = int(input("Enter a positive integer: "))
steps=0
while (c0>1):
    if (c0%2==0):
        print(c0)
        c0//=2
    else:
        print(c0)
        c0 = (3*c0)+1
    steps+=1
print("Steps =",steps)