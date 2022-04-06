#[2,5,3,4,8,1,9] swap the first and last values
thisList = [2, 5, 3, 4, 8, 1, 9]
temp = thisList[0]
thisList[0] = thisList[len(thisList) - 1]
thisList[len(thisList) - 1] = temp
print(thisList)
