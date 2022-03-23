#Take user input until user  enters "!" and sum them together
print('Enter numbers. Type "!" when you are done.')
inp = input()
sum = 0
while(inp  != '!'):
  sum = int(inp) + sum
  print('Enter numbers. Type "!" when you are done.')
  inp = input()
print(sum)
