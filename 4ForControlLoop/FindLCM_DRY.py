print('Type factor.')
factorOne=int(input())
print('Type factor.')
factorTwo=int(input())

if(factorOne == factorTwo):
    print('LCM = %d' % (factorOne))
    exit()

elif factorOne > factorTwo:
    larger = factorOne
    smaller= factorTwo
else:
    larger = factorTwo
    smaller = factorOne

if (larger % smaller ==  0):
    print('LCM = %d' % (larger))
    exit();

start = smaller
end = smaller * larger
for integer in range(start, end + 1):
    if integer % smaller == 0 and integer % larger == 0:
        print('LCM = %d' % (integer))
        exit()
