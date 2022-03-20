#Find number of digits in a given number
print('Enter number')
num = int(input())
counter = 0
while(num>0):
    counter = counter + 1
    num = int(num / 10)
print(counter)


