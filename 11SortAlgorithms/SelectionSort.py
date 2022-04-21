thisList = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
#sortedList = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
i = 0
min = 0
while i < len(thisList)-1:
    j = i
    min = i+1
    while j < len(thisList):
        if thisList[j] < thisList[min]:
            min = j
        j = j + 1
    temp = thisList[i]
    thisList[i] = thisList[min]
    thisList[min] = temp
    i = i + 1
print(thisList)