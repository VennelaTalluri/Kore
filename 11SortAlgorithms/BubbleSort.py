thisList = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
i = 0
j = 0
while j < len(thisList):
    i = 0
    while i < len(thisList)-1-j:
        if thisList[i] > thisList[i + 1]:
            plceHldr = thisList[i]
            thisList[i] = thisList[i + 1]
            thisList[i + 1] = plceHldr
        i = i + 1
    j = j + 1
print(thisList)





