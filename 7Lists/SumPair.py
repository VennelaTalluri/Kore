#[3, 5, 2, 4, 7, 1, 6]    Sum  = 8
thisList = [3, 5, 2, 4, 4, 7, 1, 6]
i = 0
while i < len(thisList):
    j = i + 1
    num1 = thisList[i]
    while j < len(thisList):
        num2 = thisList[j]
        if num1 + num2 == 8 and j != i:
            print(num1, num2)
        j = j + 1
    i = i + 1