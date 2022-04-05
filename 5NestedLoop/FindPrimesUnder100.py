divisor = 2
primeNoList = []
for integer in range(2,100):
    start = 2
    end = int(integer ** 1 / 2)
    for counter in range(start, end+1):
        if integer % counter == 0:
            break
    else:
        primeNoList.append(integer)

print(primeNoList)
