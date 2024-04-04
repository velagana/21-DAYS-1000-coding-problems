#prime numbers:
num = int(input("enter the value of num")
if num > 0:
    is_prime = True
    for i in range(2,int(num**0.5)+1):
        if i % num == 0:
            is_prime = False
        if is_prime:
            print("the num is prime")
        else:
            print("the num is not prime")
    
