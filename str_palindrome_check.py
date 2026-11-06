# checking whether a string is palindrome or not
str = input("Enter a string: ")
original = str
reversed =  str[::-1]
if original == reversed:
    print("The string is a palindrome")
else:
    print("string is not a palindrome")