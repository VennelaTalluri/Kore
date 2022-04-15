list1 = [6, 7, 9, 12, 15, 20]
list2 = [1, 2, 3, 4, 5, 8, 11, 13, 14, 17, 21, 22, 23]
i = 0
j = 0
list3 = []
while i < (len(list1)) and j < (len(list2)):
    if list1[i] <= list2[j]:
        list3.append(list1[i])
        i = i + 1
    else:
        list3.append(list2[j])
        j = j + 1
while j < len(list2):
    list3.append(list2[j])
    j = j + 1
while i < len(list1):
    list3.append(list1[i])
    i = i + 1
print(list3)