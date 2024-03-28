#Python Program for n-th Fibonacci number
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Input
n = int(input("Enter the value of n: "))

# Check for invalid input
if n < 0:
    print("Invalid input! Please enter a non-negative integer.")
else:
    result = fibonacci(n)
    print("The", n, "th Fibonacci number is:", result)
