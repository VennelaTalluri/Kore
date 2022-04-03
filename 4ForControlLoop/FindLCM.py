print('Type factor.')
factorone=int(input())   #use camel case
print('Type factor.')
factortwo=int(input())

if factorone > factortwo:
    if factorone % factortwo ==0:
        print('LCM = %d' % (factorone))
    else:  #block 1
        start = factorone
        end = factorone * factortwo
        for integer in range(start, end + 1):
            if integer % factortwo == 0 and integer % factorone == 0:
                print(integer)
                exit()
elif factorone < factortwo:
    if factortwo % factorone ==0:  # another repeatof  line7
        print('LCM = %d' % (factortwo))
    else:  #block 2 same as block 1.
        start = factortwo
        end = factorone * factortwo
        for integer in range(start, end + 1):
            if integer % factortwo == 0 and integer % factorone == 0:
                print(integer)
                exit()
else: #this is handling the case where the two numbers are equal
    print(factorone)

    #write code to avoid nesting as  far as possible.
    #test cases like division by  0 first, or in this question the == case.