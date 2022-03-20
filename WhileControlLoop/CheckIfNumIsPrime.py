print('Enter number')
num = int(input())

divisor = 2;
while(divisor>=2 and divisor<=num**1/2):
    if num % divisor == 0:
        print(divisor)
        print('Composite')
        exit()
    divisor=divisor+1
else:
    print('Prime')



