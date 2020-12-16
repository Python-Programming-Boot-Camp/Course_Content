blocks = int(input("Enter the number of blocks: "))

height = 0
next_layer=1
while (next_layer<=blocks):
    blocks-=next_layer
    height+=1
    next_layer+=1

print("The height of the pyramid:", height)