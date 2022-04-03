print("Enter number.")
num = int(input())
start = 2
end = int(num ** 1/2)
for counter in range(start, end):
    if num % counter == 0:
        print('composite')
        exit()

print("Prime")
