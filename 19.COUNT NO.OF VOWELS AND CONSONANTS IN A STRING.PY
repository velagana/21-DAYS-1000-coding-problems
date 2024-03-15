#COUNT NO.OF VOWELS AND CONSONATS IN A STRING
str = input("Enter the string: ")
count1 = 0
count2 = 0
for i in str:
if str =='A' or str =='E' or str =='I' or str =='O' or str =='U' or str =='a' or str =='e' or str =='i' or str =='o' or str =='u': 
    count1 = count1 + 1
    print(count1)
else :
    count2 = count2 + 1
    print(count2)
