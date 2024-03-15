# Define the list
my_list = [1, 2, 3, 4, 2, 2, 3, 4, 5, 2]

# Define the target element
target_element = 2

# Sort the list
my_list.sort()

# Initialize a variable to count occurrences
occurrences = 0

# Iterate through the sorted list and count occurrences of the target element
for element in my_list:
    if element == target_element:
        occurrences += 1

# Print the result
print(f"The element {target_element} occurs {occurrences} times in the list.")
