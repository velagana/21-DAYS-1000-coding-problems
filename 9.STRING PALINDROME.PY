#CHECK WHETHERTHE GIVEN STRING IS PALINDROME OR NOT
N = input("Enter the string: ")
reverse_string =  N[::-1]
if reverse_string == N:
    print("The given string is palindrome: ")
else:
    print("The given String is not a palindrome:")