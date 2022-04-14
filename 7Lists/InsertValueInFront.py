# [3,4,6,1,8,9,12] insert 5 at the beginning of the list
thisList = [3, 4, 6, 1, 8, 9, 12]
thisList.append(0)
i = len(thisList)-2
while i >= 0:
    thisList[i+1] = thisList[i]
    i=i-1
thisList[0]=5
print(thisList)