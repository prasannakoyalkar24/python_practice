# calculate gcd of two numbers
import math
num1 = int(input("Enter a number:"))
num2 = int(input("enter second number: "))
gcd = abs(num1 * num2 ) // math.lcm(num1,num2)
print(f"gcd of two numbers is : {gcd}")