myList = [1,2,3,4,5,6,7,8]
print('Type numbers. Type ! when you are done.')
inp = input()
userList = []
while inp != '!':
    userList.append(int(inp))
    print('Type numbers. Type ! when you are done.')
    inp = input()
for integerOne in myList:
    isMatch = False
    for integerTwo in userList:
        if integerOne == integerTwo:
            isMatch = True
            print('Values: %d, %d match in both lists.' % (integerOne, integerTwo))
    if(isMatch==False):
        print('Values: %d, %d DID NOT match in both lists.' % (integerOne, integerTwo))