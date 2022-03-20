print('Type a number')
num = int(input())

if num % 6 == 0:
    print('Divisible by both 2 and 3')

#inefficent
#if num % 2 == 0 & num % 3 == 0:
#    print('Divisible by both 2 and 3')


elif num % 2 == 0:
    print('Divisible by 2')

elif num % 3 == 0:
    print('Divisible by 3')

else:
    print('Divisible by neither 2 nor 3')

