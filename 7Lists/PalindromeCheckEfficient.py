print('Type word.')
userString = input()
char_array = list(userString)
i = 0
f = (len(userString)-1)
if len(char_array) % 2 == 0:
    while (i <= int(((len(char_array))-1) / 2) and f >= int((len(char_array)) / 2)):
        if (char_array[i]) == (char_array[f]):
            i = i + 1
            f = f - 1
        else:
            exit()
    print('Is palindrome.')
else:
    while (i < int(((len(char_array)-1) / 2)+1) and f > int(((len(char_array)-1) / 2)+1)):
        if (char_array[i]) == (char_array[f]):
            i = i + 1
            f = f - 1
        else:
            exit()
    print('Is palindrome.')
