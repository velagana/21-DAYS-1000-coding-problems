#creating a programme to find the fibnocci of a number
# 0,1,1,2,3,5,8,13 -- 0+1   = 1->1+1=2 -> 1+2 = 3-> 2+3= 5...This is the fibnocci numbers pattern
n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_series = []

# Initializing the first two Fibonacci numbers
fibonacci_series.append(0)
fibonacci_series.append(1)

# Generating the Fibonacci series
for i in range(2, n):
    next_fibonacci = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_fibonacci)

# Printing the Fibonacci series
print("Fibonacci series up to", n, "terms:")
for num in fibonacci_series:
    print(num, end=" ")

