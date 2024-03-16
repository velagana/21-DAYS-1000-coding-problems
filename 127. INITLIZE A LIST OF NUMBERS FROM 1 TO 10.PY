# Take input from the user
input_string = input("Enter the values separated by spaces: ")

# Split the input string into a list of integers
numbers = [int(x) for x in input_string.split()]

# Loop through a range from 0 to 10 (not 0 to 11 as in your code)
for i in range(11):
    print(i)
