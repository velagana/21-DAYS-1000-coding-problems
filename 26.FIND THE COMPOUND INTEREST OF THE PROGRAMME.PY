## COMPOUND INTEREST = A-P(1+R/100)**T
A = int(input("enter the value of A"))
p = int(input("enter the value of p"))
r = int(input("enter the value of r"))
t = int(input("enter the value of t"))
interest =  A - p * (1 + r / 100) ** t
print(interest)