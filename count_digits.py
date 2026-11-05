# count the digits in a  number
num = int(input("enter a number: "))
count = 0
while num > 0:
    i = num % 10
    count += 1
    num = num // 10
print("Total digits in number are:", count)