list_values = input("Enter the values of list: ")
listed_values = list_values.split()
listed_values = [int(x) for x in listed_values]  # Convert elements to integers if needed
minlist = min(listed_values)
maxlist = max(listed_values)
print("The minimum element in the list is:", minlist)
print("The maximum element in the list is:", maxlist)




