print('Enter numbers. Type ! when you are done.')
num = input()
sum = 0
counter = 0
while(num != '!'):
    sum = int(num) + sum
    counter = counter + 1
    print('Enter numbers. Type ! when you are done.')
    num = input()
avg = sum /counter
print(avg)