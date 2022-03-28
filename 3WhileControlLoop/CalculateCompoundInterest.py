print("Please Enter Your Preferred Interest")
interest = float(input())
print("Please Enter your Principal.")
principal = float(input())
print("Please print the duration (in years) of the account's activity.")
time = float(input())
duration = time
while(time > 0):
    time = time - 1
    principal = principal + (interest * principal)
print('New Principal is %.2f with an Interest Rate of %.2f at a duration of %.2f years' % (principal, interest, duration))