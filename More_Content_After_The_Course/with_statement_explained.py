with open("example.txt","r") as document:
    for line in document:
        print(line)

document = open("example.txt","r")
try:
    for line in document:
        print(line)
finally:
    document.close()