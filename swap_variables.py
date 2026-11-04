#swapping two numbers without a third variable
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
a,b = b,a
# print(a,",",b)
print(f" swapped values are {a} and {b}")