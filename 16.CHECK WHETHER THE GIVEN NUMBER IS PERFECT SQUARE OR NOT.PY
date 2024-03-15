# Input number
num = int(input("Enter a number: "))

# Method to check if a number is a perfect square
is_perfect_square = False

# Loop to find the perfect square
for i in range(num):
    if i * i == num:
        is_perfect_square = True
        break

# Output the result
if is_perfect_square:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
