def factorial():
    n = int(input("Enter the value of n: "))
    fact = 1

    if n < 0:
        print("The factorial for negative numbers doesn't exist.")
    elif n == 0:
        print("The factorial of zero is always one.")
    else:
        for i in range(2, n + 1):
            fact *= i
        print(f"The factorial of {n} is: {fact}")

factorial()
