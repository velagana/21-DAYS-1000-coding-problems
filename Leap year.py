#2. Create a program to determine if a given year is a leap year or not.
#THIS IS THE CODE FOR LEAP YEAR PROGRAMME:
year = int(input("Enter the year"))
if (year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
 print("The given year is Leap year")
else:
 print("The given year is not a leap year")