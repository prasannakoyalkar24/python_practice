# checking if a number is  perfect number
num = int(input("Enter a number:"))
p_sum = 0
if num <= 1:
    print("Enter a number greater than 1")
else:
    for i in range(1, (num//2) +1):
        if num % i == 0:
            p_sum += i
if num == p_sum:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")




