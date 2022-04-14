# Check if a given string is a palindrome

print('Type word.')
userString = input()
char_array = list(userString)
list = []
for index in reversed(range(len(userString))):
    list.append(userString[index])
reversedString = ''.join(list)
if userString == reversedString:
    print('Palindrome')
else:
    print('Not Palindrome')

