#GCD OF TWO NUMBERS 
num1 = int(input("enter the num1 value: "))
num2 = int(input("enter the num2 value: "))
min_value = min(num1,num2)
gcd = 1
for i in range(2,min_value+1):
    if num1 % i == 0 and num2 % i ==0:
        gcd = i
if gcd > 1:
     print("The greatest common divisor (GCD) of", num1, "and", num2, "is", gcd)
else:
    print("The greatest common divisor (GCD) of", num1, "and", num2, "is 1")


        
