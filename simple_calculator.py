a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
print("choice is 1, 2, 3, 4")
choice = int(input("Enter a choice:"))
if choice == 1 :
    print("sum of two numbers is", a+b)
elif choice == 2:
    print("Difference of two numbers is", a-b)
elif choice == 3:
    print("product of two numbers is", a * b)
elif choice == 4:
    print("Division of two numbers is",a/b)
else:
    print("Invalid choice")


