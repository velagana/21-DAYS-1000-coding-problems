def is_prime(number):
    if number <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        return is_prime

number = int(input("Enter the number: "))

if is_prime(number):
    print("The given number is a prime number")
else:
    print("The given number is not a prime number")
