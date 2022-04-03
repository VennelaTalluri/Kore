print('Enter first number.')
numOne = int(input())
print('Enter second number.')
numTwo = int(input())
if numOne == numTwo:
    print('HCF: %d' % (numOne))
    exit()

if numOne > numTwo:
    larger = numOne
    smaller = numTwo
else:
    larger = numTwo
    smaller = numOne

for integer in range(larger, 0-1, -1):
    if larger % integer == 0 and smaller % integer == 0:
        print('HCF %d' % (integer))
        exit()