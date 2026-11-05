# sum of digits of a number
num = int(input("Enter a number:"))
sum = 0
while num > 0:
i = num % 10
sum += i

print(sum)