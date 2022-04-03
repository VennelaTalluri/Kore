for integer in range(1,10 + 1):
    for integer2 in range(11,integer + 1, -1):
        print(' ', end=" ")
    for integer3 in range(1, integer + 1):
        print('*', end=" ")
    for integer4 in range(1, integer):
        print('*', end=" ")
    print('  ')