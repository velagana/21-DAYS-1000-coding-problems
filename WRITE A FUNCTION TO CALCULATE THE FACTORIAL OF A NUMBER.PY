#WRITE A FUNCTION TO FIND THE FACTORIAL OF A NUMBER!!!!
def factorial():
    n = int(input("enter the value of factorial: "))
    fact = 1
    if n < 0:
        print("the factorials do not exist for negative numbers!!!")
    elif n == 0:
        print("The factorial of zero is always one!!!!")
    else:
        for i in range(2, n + 1):
            fact = fact * i
        print(fact)

factorial()
