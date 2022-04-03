for integer in range(1, 10):
    integer2 = 1
    for integer2 in range(1, integer + 1):
        print('*', end =" ")
    print('  ')

integer = 1
while (integer<=10):
    integer2 = 1
    while (integer2 <= integer):
        print('*', end=" ")
        integer2 = integer2 + 1
    integer = integer + 1
    print('  ')