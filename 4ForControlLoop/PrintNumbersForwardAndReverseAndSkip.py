# Write a program to print numbers from 1-10  and from  10-1  and 1-100 all even numbers
start, end = 0,11
for integer in range(start, end):
    print(integer)

start, end, step = 1,11,2
for integer in range(start, end, step):
    print(integer)


start, end, step = 2,101,2
for integer in range(start, end, step):
    print(integer)

start, end, step = 10,0,-1
for integer in range(start, end, step):
    print(integer)