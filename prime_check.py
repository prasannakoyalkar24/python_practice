# Checking a number prime or not
num = int(input("Enter a number: "))
count = 0
i = 1
if num <= 1:
    print("Enter a number greater than 1")
else:
    while i <= num:
        if num  % i ==0:
            count += 1
        i += 1

    if count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")