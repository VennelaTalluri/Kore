#Take digits from user and create number until user enters "!"
print('Enter digits. Type "!" when you are done.')
inp = input()
num = 0
while(inp != '!'):
    num = (num*10) + int(inp)
    print('Enter digits. Type "!" when you are done.')
    inp = input()
print(num)