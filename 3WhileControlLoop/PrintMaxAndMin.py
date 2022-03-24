#Prompt the user to enter numbers and  use "!" to terminate. Print the max and min values of the numbers printed by the user

print('Enter numbers  and type ! when  you are finished.')
inp = input()
num = 0
if inp != '!':
    max = int(inp)
    min = int(inp)
else:
    exit()
while(inp != '!'):
    num = int(inp)
    if num > max:
        max = int(inp)
    if num < min:
        min = int(inp)
    print('Enter numbers  and type ! when  you are finished.')
    inp = input()

print('Max: %d' % (max))
print('Min: %d' % (min))
