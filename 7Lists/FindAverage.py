thisList = [1, 2, 3, 4, 5, 6]
i = 0
sum = 0
while i < len(thisList):
    sum = int(thisList[i]) + sum
    i = i + 1
avg = sum / len(thisList)
print(avg)