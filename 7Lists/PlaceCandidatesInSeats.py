list1= [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]
#list2= [1, 0, 0, 0, 1, 0, 0]
#list3 =[0, 0, 0, 0, 0, 1, 0, 0]

counter = 0

if list1[0] == 0 and list1[1] == 0:
    list1[0] = 1
    counter = counter + 1

bef = 1
mid = 2
aft = 3
while aft < len(list1):
    if list1[bef] == 0 and list1[mid] == 0 and list1[aft] == 0:
        list1[mid] = 1
        counter = counter + 1
    bef = bef + 1
    mid = mid + 1
    aft = aft + 1


if list1[len(list1)-1] == 0 and list1[len(list1)-2] == 0:
    list1[len(list1)-1] = 1
    counter = counter + 1


print(list1)
print('New seats: %d' % counter)