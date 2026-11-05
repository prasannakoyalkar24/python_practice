# checking string is a palindrome or not
str = input("Enter a string: ")
rev_str = str[::-1]
if str == rev_str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
