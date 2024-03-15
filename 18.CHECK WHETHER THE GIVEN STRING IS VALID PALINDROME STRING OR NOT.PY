#CHECK WHETHER THE GIVEN SENTENCE IS VALID PALINDROME OR NOT
str = input("Enter the string")
rev_string = str[::-1]
if str == rev_string:
    print("The given sentence is valid palindrome: ")
else:
    print("The given sentence is not a valid palindrome: ")
