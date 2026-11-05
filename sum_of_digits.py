# sum of digits of a number
num = int(input("Enter a number:"))
sum = 0
while num > 0:
    i = num % 10
    sum += i
    num = num//10

print(sum)