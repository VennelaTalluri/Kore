thisList = [2, 7, 9, 15, 25, 39, 41, 46, 54, 62, 75, 84, 97]

print('Provide number to search for')
num = int(input())
end = len(thisList)-1
mid = int((len(thisList)-1)/2)
start = 0
while start <= end:
    if num < thisList[mid]:
        end = mid
        mid = int((start+end)/2)
    elif num > thisList[mid]:
        start = mid + 1
        mid = int((start+end)/2)
    else:
        print('Found in list')