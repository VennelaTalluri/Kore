#Find the range of the list
thisList = [4, 12, 65, 5, 15, 27, 0, 34, -3, 1, 56, 7, 2]
min = thisList[0]
max = thisList[0]
for integer in (thisList):
    if integer < min:
        min = integer
    elif integer > max:
        max = integer
print('[%d,%d]' % (min, max))
