print('Enter at which natural number you would like the program to stop running.')
count = int(input())
base_n1 = 0
base_n2 = 1
print('f(0)-> %d ' % base_n1)
print('f(1)-> %d' % base_n2)
counter = 2
while(counter <= count):
  #  base_n1 = base_n2
    base_n3 = base_n2 + base_n1
    print('f(%d)–> %d' % (counter, base_n3))
    base_n1 = base_n2
    base_n2 = base_n3
    counter = counter + 1