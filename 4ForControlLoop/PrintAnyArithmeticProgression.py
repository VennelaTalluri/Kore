#Given first term (a), common difference (d) and a integer n of the Arithmetic Progression series, the task is to print the series.
#Input : a = 5, d = 2, n = 10
#Output : 5 7 9 11 13 15 17 19 21 23

print('Enter your start.')
start = int(input())
print('Enter your step.')
step = int(input())
print('Enter your end.')
end = int(input())
for integer in range(start, end + 1, step):
    print(integer)