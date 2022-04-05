thisList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if len(thisList) % 2 != 0:
    mid = int(len(thisList) / 2)
    print(thisList[mid])
else:
    mid = int((len(thisList) / 2) + 1)
    mid2 = int(len(thisList) / 2)
    avg = (thisList[mid] + thisList[mid2])/2
    print(avg)