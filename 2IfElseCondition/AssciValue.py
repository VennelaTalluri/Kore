print('Enter a character')
asciiValue = ord(input())
#print(asciiValue)

if 65 <= asciiValue and asciiValue <= 90 or asciiValue >= 97 and asciiValue <= 122:
    print('Character is an English letter')

#elif asciiValue >= 97 and asciiValue <= 122:
#    print('Character is an English letter')
else:
    print('NOT A CHARACTER')