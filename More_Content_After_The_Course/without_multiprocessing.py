import time
time1 = time.time()
for i in range (1000):
    answer = 1
    for j in range (10000):
        answer *= answer
time2 = time.time()
print(time2-time1)