print('Enter Side Length #1')
side1 = int(input())

print('Enter Side Length #2')
side2 = int(input())

print('Enter Side Length #3')
side3 = int(input())

if side1 + side2 > side3 and side3 + side2 > side1 and side3 + side1 > side2:
    print('Valid triangle')

else:
    print('not very poggers')