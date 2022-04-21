thisList = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
i = 1
while i < len(thisList):
        for j in range(i, 0, -1):
            if thisList[j] < thisList[j-1]:
                temp = thisList[j]
                thisList[j] = thisList[j - 1]
                thisList[j - 1] = temp
        i = i + 1
print(thisList)