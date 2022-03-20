print('Coefficient a')
a = int(input())

print('Coefficient b')
b = int(input())

print('Coefficient c')
c = int(input())

if b**2 - 4*a*c < 0:
    print('No solutions')

if b**2 - 4*a*c == 0:
    print('One solution: %d' % (-b / (2*a)))

if b**2 - 4*a*c > 0:
    print('Two solutions: %d , %d' % (((-b+(b**2 - 4*a*c)**1/2)/2*a), (-b-(b**2 - 4*a*c)**1/2) / (2*a)))